from urllib import request
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=35)
    correo = models.CharField(max_length=35,null=True,blank=True)
    password = models.CharField(max_length=30)


    def __str__(self):
        return self.username




# class Caso(models.Model):
#     id_caso = models.IntegerField()
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#     def __Str__(self):
#         return self.id_caso

class TipoDemanda(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Demanda(models.Model):
    id_demanda = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    hora = models.TimeField(default=timezone.now)
    tipodemanda = models.ForeignKey(TipoDemanda,null=True,blank=True,on_delete=models.CASCADE)
    detalle = models.TextField()
    #caso = models.ForeignKey(Caso,on_delete=models.CASCADE)
    rut_demandado = models.IntegerField(null=True,blank=True)
    dv_demandado = models.IntegerField(null=True,blank=True)
    nombre_demandado = models.CharField(max_length=25,null=True,blank=True)
    apellido_demandado = models.CharField(max_length=25,default='',null=True,blank=True)
    telefono_demandado = models.IntegerField(null=True,blank=True)
    comuna_demandado = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True,blank=True,related_name='comuna_demandado')
    
    rut_demandante = models.IntegerField(null=True,blank=True)
    dv_demandante = models.IntegerField(null=True,blank=True)
    nombre_demandante = models.CharField(max_length=25,null=True,blank=True)
    apellido_demandante = models.CharField(max_length=25,default='',null=True,blank=True)
    telefono_demandante = models.IntegerField(null=True,blank=True)
    comuna_demandante = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True,blank=True,related_name='comuna_demandante')

    
    def __Str__(self):
        return self.id_demanda

# class Demandado(models.Model):
#     rut = models.IntegerField()
#     dv = models.IntegerField()
#     nombre = models.CharField(max_length=25)
#     apellido = models.CharField(max_length=25)
#     telefono = models.IntegerField()
#     comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True,blank=True)

#     demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE,null=True,blank=True)

#     def __Str__(self):
#         return self.rut

# class Demandante(models.Model):
#     rut = models.IntegerField()
#     dv = models.IntegerField()
#     nombre = models.CharField(max_length=30)
#     apellido = models.CharField(max_length=30)
#     telefono = models.IntegerField()
#     comuna = models.ForeignKey(Comuna,on_delete=models.CASCADE,null=True,blank=True)

#     demanda = models.ForeignKey(Demanda, on_delete=models.CASCADE,null=True,blank=True)

#     def __Str__(self):
#         return self.rut

