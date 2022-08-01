from .models import mensaje
from django.shortcuts import render

# Create your views here.

def enviar_mensaje(request):#Funcion para enviar mensaje 
    model= mensaje()#modelo de mensaje 
    model.remitente= request.user#se obtiene el usuario que envia el mensaje 
    model.receptor= request.user#se obtiene el usuario que recibe el mensaje 
    model.contenido= request.POST['contenido']#se obtiene el contenido del mensaje 
    model.estado= False#se obtiene el estado del mensaje 
    model.save()#se guarda el mensaje 
    return render(request, 'inicio.html', {'mensaje':f"Mensaje Enviado"})#se redirecciona a la pagina de inicio con un mensaje de confirmacion 



