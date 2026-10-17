class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print("HOLA, SOY", self.nombre, "Y TENGO", self.edad, "AÑOS")


class Cliente(Persona):

    def __init__(self, nombre, edad, numeroMesa, pedido):
        super().__init__(nombre, edad)
        self.numeroMesa = numeroMesa
        self.pedido = pedido

    def realizarPedido(self):
        print("EL CLIENTE", self.nombre, "REALIZO EL PEDIDO", self.pedido)

    def cancelarPedido(self):
        print("EL CLIENTE", self.nombre, "CANCELO EL PEDIDO")


class Empleado(Persona):

    def __init__(self, nombre, edad, empleadoID, puesto):
        super().__init__(nombre, edad)
        self.empleadoID = empleadoID
        self.puesto = puesto

    def asignarTareas(self):
        print("SE ASIGNARON TAREAS AL EMPLEADO", self.nombre)

    def reportar(self):
        print("EL EMPLEADO", self.nombre, "ESTA REPORTANDO")


class Cocinero(Empleado):

    def __init__(self, nombre, edad, empleadoID, puesto, especialidad):
        super().__init__(nombre, edad, empleadoID, puesto)
        self.especialidad = especialidad

    def prepararComida(self):
        print("EL COCINERO", self.nombre, "ESTA PREPARANDO COMIDA DE", self.especialidad)


class Mesero(Empleado):

    def __init__(self, nombre, edad, empleadoID, puesto, horario):
        super().__init__(nombre, edad, empleadoID, puesto)
        self.horario = horario

    def servirMesa(self):
        print("EL MESERO", self.nombre, "ESTA SIRVIENDO LA MESA")