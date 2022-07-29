from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Categoria(models.Model):
    nombre= models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Post(models.Model):
    autor= models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    titulo= models.CharField(max_length=200)
    texto = RichTextField(blank=True, null=True)
    imagen= models.ImageField(upload_to='', blank=True)
    fecha_creacion= models.DateTimeField(default=timezone.now)

    def publicacion(self):
        self.fecha_creacion= timezone.now()
        self.save()
    
    def __str__(self):
        return self.titulo

class Avatar(models.Model):#modelo de avatar
    user= models.ForeignKey(User, on_delete=models.CASCADE)#campo usuario
    imagen= models.ImageField(upload_to='', null= True, blank=True, default='avatar_default.jpg')#campo imagen 