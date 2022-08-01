from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class mensaje():
    remitente = models.ForeignKey(User, on_delete=models.CASCADE, default=User)#Relacion con el usuario
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, default=User)#Relacion con el usuario
    contenido = models.CharField(max_length=200)#Contenido del mensaje
    estado = models.BooleanField(default=False)#False = no leido, True = leido
