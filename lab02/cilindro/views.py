from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo' : "Cilindro",
    }
    return render(request,'cilindro/index.html',context)

def calcular(request):
    if request.method == 'POST':
        
        diametro = float(request.POST.get('diametro', 0))
        altura = float(request.POST.get('altura', 0))
        volumen = 3.1416 * (diametro/2)**2 * altura
        return render(request, 'cilindro/result.html', {'resultado': volumen})
    return render(request, 'cilindro/index.html')