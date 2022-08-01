from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Avatar

# Create your views here.

def enviar_mensaje(request):#Vista para enviar mensajes
    return render(request, 'mensajeria/enviar_mensaje.html')#Renderiza la vista

def ver_mensaje (request): 
    usuario= User.objects.all() 
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url 
    return render(request, 'usuario_detalle.html', {'usuario':usuario, 'imagen':imagen}) 


def ver_mensaje(request):#Vista para ver mensajes
    return render(request, 'mensajeria/ver_mensaje.html')#Renderiza la vista
