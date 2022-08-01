from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from login.views import inicio
urlpatterns = [
    path('', inicio, name='inicio'),
    path('enviar_mensaje/', enviar_mensaje, name='enviar_mensaje'),

]