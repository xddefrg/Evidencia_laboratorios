class Billetera:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0  # cada billetera arranca en cero, con su propio saldo

    def registrar_ingreso(self, monto):
        if monto <= 0:
            return False

        self.saldo += monto
        return True

    def registrar_gasto(self, monto):
        # Se rechazan montos no positivos y gastos mayores que el saldo.
        if monto <= 0 or monto > self.saldo:
            return False

        self.saldo -= monto
        return True

    def consultar_saldo(self):
        return self.saldo


def texto(aceptado):
    return "aceptado" if aceptado else "rechazado"


ana = Billetera("Ana")
luis = Billetera("Luis")

print("Ana   - ingreso 100000:", texto(ana.registrar_ingreso(100000)))
print("Ana   - gasto 30000:   ", texto(ana.registrar_gasto(30000)))
print("Ana   - gasto 500000:  ", texto(ana.registrar_gasto(500000)))  # supera el saldo
print("Ana   - ingreso -50:   ", texto(ana.registrar_ingreso(-50)))  # monto no positivo
print("Luis  - ingreso 20000: ", texto(luis.registrar_ingreso(20000)))
print("Luis  - gasto 0:       ", texto(luis.registrar_gasto(0)))  # monto no positivo

print()
print(f"Saldo de {ana.titular}:", ana.consultar_saldo())  # 70000
print(f"Saldo de {luis.titular}:", luis.consultar_saldo())  # 20000

# Independencia: un gasto de Luis no altera el saldo de Ana.
luis.registrar_gasto(5000)
print()
print(f"Tras un gasto de Luis -> Ana: {ana.consultar_saldo()}, Luis: {luis.consultar_saldo()}")
