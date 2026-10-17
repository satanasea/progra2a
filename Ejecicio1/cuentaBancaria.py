class CuentaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __del__(self):
        print("LA CUENTA HA SIDO CERRADA")

    def depositar(self, monto):
        if monto > 0:
            self.saldo = self.saldo + monto
            print("NUEVO SALDO:", self.saldo)
        else:
            print("EL MONTO A ACREDITAR NO ES VALIDO, DEBE SER MAYOR A CERO")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            print("NUEVO SALDO:", self.saldo)
        else:
            print("SALDO INSUFICIENTE")

    def mostrarSaldo(self):
        print("SALDO ACTUAL:", self.saldo)