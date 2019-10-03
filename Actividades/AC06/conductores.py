class Conductor:
    def __init__(self, nombre, rut, mail, celular, patente):
        self.nombre = nombre
        self.rut = rut
        self.mail = mail
        self.celular = celular
        self.patente = patente


    def __str__(self):
        nombre = f"Nombre conductor: {self.nombre}\n"
        rut = f"Rut: {self.rut}\n"
        mail = f"Mail: {self.mail}\n"
        celular = f"Celular: {self.celular}\n"
        patente =  f"Patente: {self.patente}\n"

        return nombre + rut + mail + celular + patente + "\n"
