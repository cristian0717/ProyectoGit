from django.http import HttpResponse
from django.shortcuts import render
from AppLiniers.models import Defensor, Medio, Delantero


def defensor (self):
    defensor = Defensor (nombre="Federico", apellido="Ezcurra", edad=27, puesto=2)
    defensor.save()
    documento = f"Mi nombre es {defensor.nombre}, {defensor.apellido}, tengo {defensor.edad} años y juego de {defensor.puesto}"
    return HttpResponse (documento)

def medio (self):
    medio=Medio (nombre="Marcelo", apellido="Salandra", edad=27, puesto=8)
    medio.save()
    archivo = f"Mi nombre es {medio.nombre}, {medio.apellido}, tengo {medio.edad} años y juego de {medio.puesto}"
    return HttpResponse (archivo)

def delantero (self):
    delantero = Delantero(nombre="Cristian", apellido="Vega", edad=26, puesto=9)
    delantero.save()
    retorno = f"Mi nombre es {delantero.nombre}, {delantero.apellido}, tengo {delantero.edad} años y juego de {delantero.puesto}"
    return HttpResponse (retorno)

    
