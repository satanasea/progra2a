from cuentaBancaria import CuentaBancaria

cB1 = CuentaBancaria("JUAN MA", 1000)

cB1.mostrarSaldo()

cB1.depositar(500)

cB1.retirar(200)

cB1.retirar(2000)

cB1.depositar(0)

cB1.mostrarSaldo()