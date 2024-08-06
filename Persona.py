class Persona:

    def __init__(self,nombre,apellido,telefono,mail,dni):
        self.nombre   = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.mail     = mail
        self.dni      = dni

    def __str__(self):
        return self.nombre,self.apellido
    
    def datosTitular(self):
        return f"DATOS DEL TITULAR: {self.nombre} {self.apellido}."
    