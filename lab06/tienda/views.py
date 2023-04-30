from django.shortcuts import render, get_object_or_404
from . models import Producto,Categoria
# Create your views here.

def index(request):
    product_list = Producto.objects.order_by('nombre')[:6]
    categorias_list = Categoria.objects.all()
    context = {
        'product_list':product_list,
        'categorias': categorias_list
    }
    return render(request,'index.html',context)

def producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    categorias_list = Categoria.objects.all()
    return render(request,'producto.html',{'producto':producto,'categorias': categorias_list})

def categoria(request, categoria_id):
    categorias_list = Categoria.objects.all()
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    productos = Producto.objects.filter(categoria_id=categoria_id)
    context = {'categoria':categoria,'categorias': categorias_list, 'productos':productos}
    return render(request, 'categoria.html',context)