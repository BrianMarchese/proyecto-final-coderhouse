from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from login.views import inicio
urlpatterns = [
    path('', inicio, name='inicio'),
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),#se crea la ruta para enviar mensaje
    path('leer_un_mensaje/', leer_mensajes, name='ver_mensajes'),#se crea la ruta para leer un mensaje
    path('leer_mensajes/', leer_mensajes, name='ver_mensajes'),#se crea la ruta para ver mensajes
]