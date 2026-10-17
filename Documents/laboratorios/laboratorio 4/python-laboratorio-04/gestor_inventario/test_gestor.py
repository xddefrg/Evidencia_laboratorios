"""Pruebas automáticas del gestor (tabla 16 y pruebas 17 y 18 del laboratorio).

Se ejecutan desde esta carpeta con:  python -m unittest -v
Usan carpetas temporales: nunca tocan datos/productos.json real.
"""
import csv
import json
import tempfile
import unittest
from pathlib import Path

from almacenamiento import ErrorAlmacenamiento, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import Producto
from reportes import exportar_csv


def producto(codigo="P001", nombre="Teclado", categoria="Periféricos", precio=85000, cantidad=4):
    return Producto(codigo, nombre, categoria, precio, cantidad)


def inventario_de_prueba():
    inv = Inventario()
    inv.registrar(producto("P001", "Teclado", "Periféricos", 85000, 4))
    inv.registrar(producto("P002", "Mouse", "Periféricos", 45000, 0))
    inv.registrar(producto("P003", "Monitor", "Componentes", 700000, 2))
    return inv


class BaseConTemporal(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.dir = Path(self._tmp.name)
        self.ruta = self.dir / "datos" / "productos.json"


class PruebasProducto(unittest.TestCase):
    def test_producto_valido(self):
        p = producto()
        self.assertEqual((p.codigo, p.precio, p.cantidad), ("P001", 85000.0, 4))

    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            producto(nombre="   ")

    def test_categoria_desconocida(self):
        with self.assertRaises(ValueError):
            producto(categoria="Muebles")

    def test_precios_invalidos(self):
        for precio in (0, -1, -85000, float("nan"), float("inf"), float("-inf"), "100", None, True, 10**400):
            with self.subTest(precio=precio):
                with self.assertRaises(ValueError):
                    producto(precio=precio)

    def test_cantidades_invalidas(self):
        for cantidad in (-1, 1.5, "3", None, True):
            with self.subTest(cantidad=cantidad):
                with self.assertRaises(ValueError):
                    producto(cantidad=cantidad)

    def test_cantidad_cero_se_acepta(self):
        self.assertTrue(producto(cantidad=0).sin_stock)

    def test_actualizar_cantidad_rechazada_no_cambia_el_estado(self):
        p = producto(cantidad=4)
        with self.assertRaises(ValueError):
            p.actualizar_cantidad(-3)
        self.assertEqual(p.cantidad, 4)

    def test_ida_y_vuelta_diccionario(self):
        original = producto()
        copia = Producto.desde_diccionario(original.a_diccionario())
        self.assertEqual(original.a_diccionario(), copia.a_diccionario())
        self.assertIsNot(original, copia)

    def test_desde_diccionario_aplica_validaciones(self):
        datos = producto().a_diccionario()
        datos["precio"] = -5
        with self.assertRaises(ValueError):
            Producto.desde_diccionario(datos)

    def test_desde_diccionario_estructura_inesperada(self):
        with self.assertRaises(ValueError):
            Producto.desde_diccionario({"codigo": "P001"})  # faltan campos
        with self.assertRaises(ValueError):
            Producto.desde_diccionario("no es un objeto")
        extra = producto().a_diccionario()
        extra["color"] = "negro"
        with self.assertRaises(ValueError):
            Producto.desde_diccionario(extra)


class PruebasInventario(unittest.TestCase):
    def test_codigo_duplicado_se_rechaza(self):
        inv = Inventario()
        inv.registrar(producto("P001"))
        with self.assertRaises(ValueError):
            inv.registrar(producto("P001", nombre="Otro"))
        self.assertEqual(len(inv), 1)

    def test_actualizar_y_eliminar(self):
        inv = inventario_de_prueba()
        inv.actualizar_existencias("P002", 5)
        self.assertEqual(inv.buscar("P002").cantidad, 5)
        inv.eliminar("P003")
        self.assertIsNone(inv.buscar("P003"))

    def test_actualizar_con_cantidad_negativa_no_modifica(self):
        inv = inventario_de_prueba()
        with self.assertRaises(ValueError):
            inv.actualizar_existencias("P001", -1)
        self.assertEqual(inv.buscar("P001").cantidad, 4)

    def test_codigo_inexistente(self):
        inv = inventario_de_prueba()
        with self.assertRaises(ValueError):
            inv.actualizar_existencias("NOPE", 1)
        with self.assertRaises(ValueError):
            inv.eliminar("NOPE")

    def test_listar_no_expone_la_coleccion_interna(self):
        inv = inventario_de_prueba()
        inv.listar().clear()
        self.assertEqual(len(inv), 3)

    def test_prueba_numerica_17(self):
        inv = inventario_de_prueba()
        r = inv.resumen()
        self.assertEqual(r["productos"], 3)
        self.assertEqual(r["unidades"], 6)
        self.assertEqual(r["valor_total"], 1740000.0)
        self.assertEqual(r["sin_existencias"], ["Mouse"])
        self.assertEqual(r["categorias_utilizadas"], 2)

        inv.actualizar_existencias("P002", 5)
        r = inv.resumen()
        self.assertEqual(r["unidades"], 11)
        self.assertEqual(r["valor_total"], 1965000.0)

    def test_carga_con_codigo_repetido_no_es_parcial(self):
        datos = [producto("P001").a_diccionario(), producto("P001").a_diccionario()]
        with self.assertRaises(ValueError):
            Inventario.desde_datos(datos)

    def test_carga_con_un_registro_invalido_no_es_parcial(self):
        malo = producto("P002").a_diccionario()
        malo["cantidad"] = -4
        datos = [producto("P001").a_diccionario(), malo]
        with self.assertRaises(ValueError):
            Inventario.desde_datos(datos)


class PruebasAlmacenamiento(BaseConTemporal):
    def test_primera_ejecucion_json_inexistente(self):
        inv = cargar_inventario(self.ruta)
        self.assertEqual(len(inv), 0)
        self.assertFalse(self.ruta.exists())  # cargar nunca crea archivos

    def test_guardar_y_recuperar(self):
        guardar_inventario(inventario_de_prueba(), self.ruta)
        datos = json.loads(self.ruta.read_text(encoding="utf-8"))
        self.assertEqual([d["codigo"] for d in datos], ["P001", "P002", "P003"])
        self.assertEqual(datos[0]["precio"], 85000.0)

        recuperado = cargar_inventario(self.ruta)
        self.assertEqual(recuperado.exportar_datos(), inventario_de_prueba().exportar_datos())

    def test_no_queda_archivo_temporal(self):
        guardar_inventario(inventario_de_prueba(), self.ruta)
        self.assertEqual([p.name for p in self.ruta.parent.iterdir()], ["productos.json"])

    def test_cambios_persisten_tras_reiniciar(self):
        inv = inventario_de_prueba()
        guardar_inventario(inv, self.ruta)

        inv = cargar_inventario(self.ruta)  # "reinicio"
        inv.actualizar_existencias("P002", 5)
        inv.eliminar("P003")
        guardar_inventario(inv, self.ruta)

        inv = cargar_inventario(self.ruta)  # segundo "reinicio"
        self.assertEqual(inv.buscar("P002").cantidad, 5)
        self.assertIsNone(inv.buscar("P003"))

    def test_caracteres_especiales_utf8(self):
        inv = Inventario()
        inv.registrar(producto("P001", "Cámara ñandú", "Periféricos"))
        guardar_inventario(inv, self.ruta)
        texto = self.ruta.read_text(encoding="utf-8")
        self.assertIn("Cámara ñandú", texto)  # ensure_ascii=False
        self.assertEqual(cargar_inventario(self.ruta).buscar("P001").nombre, "Cámara ñandú")

    def _escribir_y_verificar_intacto(self, contenido):
        self.ruta.parent.mkdir(parents=True, exist_ok=True)
        self.ruta.write_text(contenido, encoding="utf-8")
        with self.assertRaises(ErrorAlmacenamiento):
            cargar_inventario(self.ruta)
        # El archivo dañado se conserva exactamente como estaba.
        self.assertEqual(self.ruta.read_text(encoding="utf-8"), contenido)

    def test_json_con_sintaxis_incorrecta(self):
        self._escribir_y_verificar_intacto(
            '[{"codigo": "P001", "nombre": "Teclado"}\n{"codigo": "P002"}]'
        )

    def test_json_vacio_se_trata_como_danado(self):
        self._escribir_y_verificar_intacto("")

    def test_json_con_estructura_inesperada(self):
        self._escribir_y_verificar_intacto('{"productos": []}')
        self._escribir_y_verificar_intacto('["P001", "P002"]')

    def test_json_con_registro_invalido(self):
        malo = producto().a_diccionario()
        malo["categoria"] = "Muebles"
        self._escribir_y_verificar_intacto(json.dumps([malo]))

    def test_json_con_nan_en_precio(self):
        self._escribir_y_verificar_intacto(
            '[{"codigo":"P001","nombre":"X","categoria":"Accesorios","precio":NaN,"cantidad":1}]'
        )

    def test_json_con_codigo_repetido(self):
        d = producto().a_diccionario()
        self._escribir_y_verificar_intacto(json.dumps([d, d]))

    def test_error_de_escritura_se_informa(self):
        bloqueo = self.dir / "es_un_archivo"
        bloqueo.write_text("x", encoding="utf-8")
        ruta_imposible = bloqueo / "productos.json"  # "carpeta" que en realidad es un archivo
        with self.assertRaises(ErrorAlmacenamiento):
            guardar_inventario(inventario_de_prueba(), ruta_imposible)

    def test_fallo_al_guardar_conserva_el_original(self):
        guardar_inventario(inventario_de_prueba(), self.ruta)
        antes = self.ruta.read_text(encoding="utf-8")
        # Un directorio con el nombre del temporal hace fallar la escritura.
        (self.ruta.parent / "productos.json.tmp").mkdir()
        with self.assertRaises(ErrorAlmacenamiento):
            guardar_inventario(Inventario(), self.ruta)
        self.assertEqual(self.ruta.read_text(encoding="utf-8"), antes)


class PruebasReportes(BaseConTemporal):
    def test_csv_con_encabezados_y_valores(self):
        inv = inventario_de_prueba()
        inv.actualizar_existencias("P002", 5)
        ruta = exportar_csv(inv, self.dir / "reportes" / "inventario.csv")

        with ruta.open("r", newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            self.assertEqual(
                lector.fieldnames,
                ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"],
            )
            filas = {fila["codigo"]: fila for fila in lector}

        self.assertEqual(float(filas["P001"]["valor_inventario"]), 340000.0)
        self.assertEqual(float(filas["P002"]["valor_inventario"]), 225000.0)
        self.assertEqual(float(filas["P003"]["valor_inventario"]), 1400000.0)
        # Es precio * cantidad, no la suma ni el precio unitario.
        self.assertNotEqual(float(filas["P001"]["valor_inventario"]), 85000.0)

    def test_exportar_no_modifica_el_inventario(self):
        inv = inventario_de_prueba()
        antes = inv.exportar_datos()
        exportar_csv(inv, self.dir / "r.csv")
        self.assertEqual(inv.exportar_datos(), antes)


if __name__ == "__main__":
    unittest.main(verbosity=2)
