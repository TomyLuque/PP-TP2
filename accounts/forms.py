# Form de registro con captcha. Bastante tranqui.
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class RegistroForm(UserCreationForm):
    # Agrego captcha para que no se registren bots re densos.
    captcha = CaptchaField(label='no soy un robot')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
