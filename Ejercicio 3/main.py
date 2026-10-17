class Persona:

    def __init__(self, apellidos, nombres, fechaDeNacimiento):
        self.apellidos = apellidos
        self.nombres = nombres
        self.fechaDeNacimiento = fechaDeNacimiento

    def __str__(self):
        return "APELLIDOS: " + self.apellidos + "\nNOMBRES: " + self.nombres + "\nFECHA DE NACIMIENTO: " + self.fechaDeNacimiento

class Alumno(Persona):

    def __init__(self, apellidos, nombres, fechaDeNacimiento, carne, fechaInscripcion, carrera, jornada):
        super().__init__(apellidos, nombres, fechaDeNacimiento)
        self.carne = carne
        self.fechaInscripcion = fechaInscripcion
        self.carrera = carrera
        self.jornada = jornada

    def __str__(self):
        return "APELLIDOS: " + self.apellidos + "\nNOMBRES: " + self.nombres + "\nFECHA DE NACIMIENTO: " + self.fechaDeNacimiento + "\nCARNE: " + self.carne + "\nFECHA DE INSCRIPCION: " + self.fechaInscripcion + "\nCARRERA: " + self.carrera + "\nJORNADA: " + self.jornada

persona = Persona("US STRATTON", "GABRIEL LESTER", "07/01/2006")
alumno = Alumno("FERGUSSON MORALES", "ESTEFAN MAXCIMILIANO", "18/10/2026", "1010-26-22427", "01/02/2026", "INGENIERIA CIVIL", "MATUTINA")

print(persona)
print()
print(alumno)