class Persona:
    # constructor
    def __init__(self,nombre,apellido,edad,estatura,estado_civil=None):
        # dar personalidad al objeto
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estado_civil = estado_civil
        self.estatura = estatura
        # print(f"Nacio {nombre}")
    
    # comportamientos
    def saludar(self):
        print(f"Hola soy {self.nombre}")
    
    def hablar(self,mensaje):
        print(f"{self.nombre}: {mensaje}")
    
    def estadoCivil(self,persona):
        self.estado_civil = persona
    
    def esposo(self):
        print(f"{self.nombre} esposo: {self.estado_civil.nombre}" if self.estado_civil else f"{self.nombre}: No tengo")
    
    def __str__(self):
        return f"hola soy {self.nombre}"