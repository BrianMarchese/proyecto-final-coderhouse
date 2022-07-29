from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirme la contraseña', widget=forms.PasswordInput)

    first_name= forms.CharField(max_length=50)
    last_name= forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name'] 
        help_texts = {k:"" for k in fields}

class Avatar_Form(forms.Form):#formulario de avatar
    imagen = forms.ImageField(label='imagen')#se agrega el campo imagen