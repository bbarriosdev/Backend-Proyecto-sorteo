from django.db import models
import uuid
class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(max_length=254)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True) 
    contrasena = models.CharField(max_length=255, blank=True, null=True)  


    def __str__(self):
        return self.nombre
