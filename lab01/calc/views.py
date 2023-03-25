from django.shortcuts import render
from django.http import HttpResponse

opers = {
    'suma' : '+',
    'resta' : '-',
    'producto' : '*',
    'division' : '/'
}

def index(request):
    return render(request,'index.html')

def calcular(request, oper, num1, num2):
    try:
        res = eval(f"{num1} {opers[oper]} {num2}")
        context = {'num1': num1, 'num2': num2, 'result': res, 'oper' : oper}
        return render(request, 'calc.html',context)
    except:
        message = "Error al calcular o al ingresar la operación"
        return HttpResponse(message)