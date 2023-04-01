from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo' : "Calculadora",
    }
    return render(request,'calculadora/index.html',context)

def calcular(request):
    if request.method == 'POST':
        
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        operacion = request.POST.getlist('operacion', '')
        
        if 'suma' in operacion:
            resultado = num1 + num2
        
        elif 'resta' in operacion:
            resultado = num1 - num2
        
        elif 'multiplicacion' in operacion:
            resultado = num1 * num2
        
        return render(request, 'calculadora/result.html', {'resultado': resultado})
    return render(request, 'calculadora/index.html')