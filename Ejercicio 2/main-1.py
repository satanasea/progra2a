from clases import Persona, Cliente, Empleado, Cocinero, Mesero

persona = Persona("MAJO", 19)
cliente = Cliente("JOSE", 20, 5, 10)
empleado = Empleado("ALEJANDRO", 19, 101, "ADMINISTRADOR")
cocinero = Cocinero("ARNOLD", 19, 102, "COCINERO", "ITALIANA")
mesero = Mesero("EMERSON", 19, 103, "MESERO", "MATUTINO")

persona.presentarse()

cliente.presentarse()
cliente.realizarPedido()
cliente.cancelarPedido()

empleado.presentarse()
empleado.asignarTareas()
empleado.reportar()

cocinero.presentarse()
cocinero.asignarTareas()
cocinero.reportar()
cocinero.prepararComida()

mesero.presentarse()
mesero.asignarTareas()
mesero.reportar()
mesero.servirMesa()
