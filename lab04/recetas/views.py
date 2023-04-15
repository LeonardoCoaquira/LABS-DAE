from django.shortcuts import render, get_object_or_404
from .models import Receta, Comentario

# Create your views here.
def lista_recetas(request):
    # Obtener todas las recetas de la base de datos
    recetas = Receta.objects.all()
    
    # Pasar las recetas a la plantilla como contexto
    context = {'recetas': recetas}
    
    # Renderizar la plantilla recetas.html con el contexto
    return render(request, 'detalle_receta.html', context)

def detalle_receta(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    comentarios = Comentario.objects.filter(receta=receta)
    return render(request, 'recetaUnica.html', {'receta': receta, 'comentarios': comentarios})   