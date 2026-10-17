class Persona:
    def __init__(self,pNombre, pEdad, pDireccion):
        self.nombre = pNombre
        self.edad = pEdad
        self.direccion = pDireccion

    def __str__(self):
        return f"NOMBRE:{self.nombre} EDAD:{self.edad} DIRECCION:{self.direccion}"

class Estudiante(Persona):
    def __init__(self, pCodigo, pGrado, pPromedio,pNombre, pEdad, pDireccion):
        #Persona.__init__(self, pNombre,pEdad,pDireccion)
        super().__init__(pNombre,pEdad,pDireccion)
        self.codigo = pCodigo
        self.grado = pGrado
        self.promedio = pPromedio

    def __str__(self):
        return super().__str__() + " " + f"CODIGO:{self.codigo} GRADO:{self.grado} PROMEDIO:{self.promedio}"

class Docente(Persona):
    #constructor
    def __init__(self, pEspecialidad, pSalario, pAniosExp,
                       pNombre, pEdad, pDireccion):
        #atributos
        #Activacion 01
        #Persona.__init__(self,pNombre, pEdad,pDireccion)
        #Activacion 02
        super().__init__(pNombre, pEdad,pDireccion)
        self.especialidad = pEspecialidad
        self.salario = pSalario
        self.aniosExperiencia = pAniosExp
  
class Tutor(Docente):
     def __init__(self, pGrupo, pReuniones, pApoyo, 
                  pEspecialidad, pSalario, pAniosExp,  
                  pNombre, pEdad, pDireccion):

        #Docente.__init__(self,pEspecialidad, pSalario, pAniosExp,
        #                         pNombre, pEdad, pDireccion)       
        super().__init__(pEspecialidad, pSalario, pAniosExp,
                         pNombre, pEdad, pDireccion)
        self.grupo = pGrupo
        self.reuniones = pReuniones
        self.apoyo = pApoyo