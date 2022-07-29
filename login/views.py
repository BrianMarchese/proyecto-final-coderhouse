from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from login.forms import UserRegisterForm, UserEditForm
from .models import Categoria, Post, Avatar
from django.views.generic import DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.


def inicio(request): #vista de inicio
    imagen = Avatar.objects.filter(user=request.user.id)[0].imagen.url
    return render (request, "inicio.html", {'imagen':imagen})

def login_request(request): # vista para loguear
    if request.method=="POST":#si el metodo es post
        form= AuthenticationForm(request, data=request.POST)#se crea un formulario con los datos del request
        if form.is_valid:#si el formulario es valido
            usu= request.POST['username']#se obtiene el usuario
            clave= request.POST['password']#se obtiene la clave

            usuario= authenticate(username=usu, password=clave)#se autentica el usuario

            if usuario is not None:#si el usuario no es nulo
                login(request, usuario)#se loguea el usuario
                return render(request, 'inicio.html', {'form':form, 'mensaje':f"Bienvenido {usuario}"})# se redirecciona a la pagina de inicio
            else:#si el usuario es nulo
                return render(request, 'login.html', {'form':form, 'mensaje':f"Usuario o contraseña incorrectos"})#se redirecciona a la pagina de login
        else:#si el formulario no es valido
            return render(request, 'login.html', {'form':form, 'mensaje':f"FORMULARIO INVALIDO"})#se redirecciona a la pagina de login
    else:#si el metodo no es post
        form= AuthenticationForm()#se crea un formulario
        return render(request, 'login.html', {'form':form})#se redirecciona a la pagina de login

def register(request):#vista para registrar
    if request.method == 'POST':#si el metodo es post
        form= UserRegisterForm(request.POST)#se crea un formulario con los datos del request
        if form.is_valid():#si el formulario es valido
            username= form.cleaned_data["username"]#se obtiene el usuario

            form.save()#se guarda el usuario
            return render(request, 'inicio.html', {'form':form, 'mensaje':f"Usuario Creado: {username}"})#se redirecciona a la pagina de inicio
    else:#si el metodo no es post
        form= UserRegisterForm()#se crea un formulario
    return render (request, 'register.html', {'form':form})#se redirecciona a la pagina de registro

@login_required
def electricos(request):
    posts= Post.objects.all()
    return render(request, 'electricos.html', {'posts':posts})

class Electrico_detalle(DetailView, LoginRequiredMixin):
    model= Post
    template_name= "electrico_detalle.html"

class Electrico_creacion(CreateView, LoginRequiredMixin):
    model= Post
    fields= ['autor','titulo', 'texto', 'imagen', 'fecha_creacion']
    template_name= 'electrico_form.html'
    success_url= reverse_lazy("electricos")

def eliminar_electrico(request, post_titulo): #vista de eliminar electricos
    post= Post.objects.get(titulo=post_titulo)#se obtiene el post
    post.delete()#se elimina el post

    postt= Post.objects.all()
    return render(request, 'inicio.html', {"postt":postt}) # lo dejo que retorne a inicio.html porque al retornal a electricos.html no me muestra los autos, revisar eso


class Electrico_editar(UpdateView, LoginRequiredMixin):
    model= Post
    fields= ['autor','titulo', 'texto', 'imagen', 'fecha_creacion']
    template_name= 'electrico_form.html'
    success_url= reverse_lazy("electricos")

def about(request):
    return render(request, "about.html")

def editar_Perfil(request):
    usuario=request.user

    if request.method =='POST':
        formulario=UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']
            usuario.save()

            return render(request, 'inicio.html', {'usuario':usuario, 'mensaje':'PERFIL EDITADO EXITOSAMENTE'})
    else:
        formulario=UserEditForm(instance=usuario)
    return render(request, 'editar_perfil.html', {'formulario':formulario, 'usuario':usuario.username})


@login_required
def usuario_detalle(request): #vista para detalle de usuario
    imagen = Avatar.objects.filter(user=request.user.id)[0].imagen.url
    usuario= User.objects.all() #se obtiene el usuario
    return render(request, 'usuario_detalle.html', {'usuario':usuario, 'imagen':imagen}) #vista para crear un post