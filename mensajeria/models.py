from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class mensaje():
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, default=User)#Relacion con el usuario que envia el mensaje
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, default=User)#Relacion con el usuario que recibe el mensaje
    contenido = models.TextField()#Contenido del mensaje
    leido = models.BooleanField(default=False)#False = no leido, True = leido 
