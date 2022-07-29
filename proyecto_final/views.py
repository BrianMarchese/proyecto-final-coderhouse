from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from login.models import Avatar
def inicio(request): #vista de inicio
    imagen= Avatar.objects.filter(user= request.user.id)[0].imagen.url
    return render (request, "inicio.html", {'imagen':imagen})

