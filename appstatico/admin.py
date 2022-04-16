from django.contrib import admin
from .models import Demanda,TipoDemanda,Comuna,Profile

admin.site.register(Demanda)
# admin.site.register(Demandado)
# admin.site.register(Demandante)
admin.site.register(TipoDemanda)
admin.site.register(Comuna)
admin.site.register(Profile)