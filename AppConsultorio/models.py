from django.db import models

class medico(models.Model):

    
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    matricula = models.IntegerField()


    def __str__(self) -> str:
        return f"Medico: {self.apellido} {self.nombre}, {self.especialidad}, Matricula numero: {self.matricula}"
    
    


class paciente(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    obra_social = models.CharField(max_length=30)
    dni = models.IntegerField()

    
    


class usuario(models.Model): 
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()

    def __str__(self) -> str:
        return f"Usuario: {self.apellido} {self.nombre}, DNI: {self.documento}"
