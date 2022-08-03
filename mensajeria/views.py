from .models import mensaje
from django.shortcuts import render

# Create your views here.

def crear_mensaje(request):#Funcion para crear mensaje 
    return render(request, 'crear_mensaje.html')

def enviar_mensaje(request):#Funcion para enviar mensaje 
    model= mensaje()#modelo de mensaje 
    model.remitente= request.user#se obtiene el usuario que envia el mensaje 
    model.receptor= request.user#se obtiene el usuario que recibe el mensaje 
    model.contenido= request.POST['contenido']#se obtiene el contenido del mensaje 
    model.estado= False#se obtiene el estado del mensaje 
    model.save()#se guarda el mensaje 
    return render(request, 'inicio.html', {'mensaje':f"Mensaje Enviado"})#se redirecciona a la pagina de inicio con un mensaje de confirmacion 

def leer_mensajes(request):#Funcion para ver los mensajes 
    mensajes= mensaje.objects.filter(remitente=request.user)#se obtienen los mensajes del usuario 
    return render(request, 'mensajes.html', {'mensajes':mensajes})#se redirecciona a la pagina de mensajes con los mensajes obtenidos

def leer_mensaje(request, id):#Funcion para ver un mensaje 
    mensaje= mensaje.objects.get(id=id)#se obtiene el mensaje 
    mensaje.estado= True#se cambia el estado del mensaje 
    mensaje.save()#se guarda el mensaje 
    return render(request, 'mensaje.html', {'mensaje':mensaje})#se redirecciona a la pagina de mensaje con el mensaje obtenido

