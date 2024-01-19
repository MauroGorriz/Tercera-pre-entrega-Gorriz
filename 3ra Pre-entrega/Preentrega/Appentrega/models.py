from django.db import models

##Las clases en si tienen elementos comunes,
##pero a la vez varian en construccion, rendimiento y variables maximas alcanzables##

#Clase Bomba Centrifuga
class BCentri(models.Model):
    modelo = models.CharField(max_length=40)
    materiales_carcaza = models.CharField(max_length=40)
    materiales_voluta = models.CharField(max_length=40)
    presion = models.IntegerField()
    caudal = models.IntegerField()
    altura = models.IntegerField()
    temp = models.IntegerField()

#Clase Bomba de tornillo
    
class Btornillo(models.Model):
    modelo = models.CharField(max_length=40)
    materiales_carcaza = models.CharField(max_length=40)
    materiales_tornillo = models.CharField(max_length=40)
    presion = models.IntegerField()
    caudal = models.IntegerField()
    altura = models.IntegerField()
    temp = models.IntegerField()

#Clase Bomba de engranajes

class Bengranajes(models.Model):
    modelo = models.CharField(max_length=40)
    materiales_carcaza = models.CharField(max_length=40)
    materiales_engranajes = models.CharField(max_length=40)
    presion = models.IntegerField()
    caudal = models.IntegerField()
    altura = models.IntegerField()
    temp = models.IntegerField()