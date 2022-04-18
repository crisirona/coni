from django import forms

from .models import Demanda
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class DemandaForm(forms.ModelForm):

    class Meta:
        model = Demanda
        fields = ('id_demanda', 'fecha','hora','tipodemanda','detalle',
                    'rut_demandado', 'dv_demandado','nombre_demandado','apellido_demandado','telefono_demandado','comuna_demandado',
                    'rut_demandante', 'dv_demandante','nombre_demandante','apellido_demandante','telefono_demandante','comuna_demandante')


# class DemandadoForm(forms.ModelForm):

#     class Meta:
#         model = Demandado
#         fields = ('rut', 'dv','nombre','apellido','telefono','comuna')


# class DemandanteForm(forms.ModelForm):

#     class Meta:
#         model = Demandante
#         fields = ('rut', 'dv','nombre','apellido','telefono','comuna')

class Registro(UserCreationForm):
    pass

class CustomUserCreationForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ['last_name','username','email','password1','password2']
    
  