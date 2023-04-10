from django.shortcuts import render
from .models import Receta

# Create your views here.
def lista_recetas(request):
    # Obtener todas las recetas de la base de datos
    recetas = Receta.objects.all()
    
    # Pasar las recetas a la plantilla como contexto
    context = {'recetas': recetas}
    
    # Renderizar la plantilla recetas.html con el contexto
    return render(request, 'recetas.html', context)
