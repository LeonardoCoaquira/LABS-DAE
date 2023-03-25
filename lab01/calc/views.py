from django.shortcuts import render
from django.http import HttpResponse

opers = {
    'suma' : '+',
    'resta' : '-',
    'producto' : '*',
    'division' : '/'
}

def index(request):
    return HttpResponse("<h1>Estás dentro de la Calculadora!</h1>")

def calcular(request, oper, num1, num2):
    try:
        res = eval(f"{num1} {opers[oper]} {num2}")
        message = f"La {oper} de {num1} {opers[oper]} {num2} = {res}"
    except:
        message = "Error al calcular o al ingresar la operación"
    return HttpResponse(message)