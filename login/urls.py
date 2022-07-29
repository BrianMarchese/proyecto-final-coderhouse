from django.contrib import admin
from django.urls import path
from .views import *
from login.views import inicio
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('electricos/', electricos, name='electricos'),
    path('electrico/<pk>', Electrico_detalle.as_view(), name='electrico_detalle'),
    path('electrico/nuevo/', Electrico_creacion.as_view(), name='electrico_creacion'),
    path('eliminar_electrico/<post_titulo>', eliminar_electrico, name='eliminar_electrico'),
    path('electrico/editar/<pk>', Electrico_editar.as_view(), name='electrico_editar'),
    path('about/', about, name='about'),
    path('editar_perfil/', editar_Perfil, name='editar_perfil'),
    path('usuario_detalle/', usuario_detalle, name='usuario_detalle'),
    
]