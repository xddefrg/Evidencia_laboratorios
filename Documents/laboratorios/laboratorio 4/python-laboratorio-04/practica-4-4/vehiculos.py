# Práctica 4.4 - Ejercicio: Vehículos.
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindraje):
        super().__init__(marca, modelo)  # reutiliza marca y modelo
        self.cilindraje = cilindraje


moto1 = Motocicleta("Yamaha", "MT-03", 321)
moto2 = Motocicleta("Honda", "CB190R", 184)

for moto in (moto1, moto2):
    print(f"Marca: {moto.marca} | Modelo: {moto.modelo} | Cilindraje: {moto.cilindraje} cc")
