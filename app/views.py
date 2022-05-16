from django.shortcuts import redirect, render

from .models import *
from .forms import *
# Create your views here.


def index(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    

    return render(request,'app/index.html', datos)

def agregarproducto(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente"
    return render(request,'app/productos/agregarproducto.html', datos)

def modificarProductos(request, plu_codigo):
    producto = Producto.objects.get(plu_codigo=plu_codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST' :
        formulario = ProductoForm(request.POST,files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto Modifcado correctamente"
            datos['form'] = formulario
    return render(request,'app/productos/modificarProductos.html', datos)

def listarProductos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    

    return render(request,'app/productos/listarProductos.html', datos)

def eliminarProducto(request, plu_codigo):
    producto =Producto.objects.get(plu_codigo=plu_codigo)
    producto.delete()

    return redirect(to="listarProductos")
 


def index_sesion_iniciada(request):
    productosAll = Producto.objects.all()
    datos = {
        'listarProductos' : productosAll
    }

    if request.method == 'POST':
        carrito = Items_carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()



    return render(request,'app/index_sesion_iniciada.html', datos)

def carrito(request):
    productosAll = Producto.objects.all()
    productosAll = Items_carrito.objects.all()
    datos = {
        'listarProductos' : productosAll
    }
    return render(request,'app/carrito.html', datos)

def segumiento_de_compra(request):
    return render(request,'app/segumiento_de_compra.html')

def historial(request):
    return render(request,'app/historial.html')
    
def crear_usuario(request):
    return render(request,'app/crear_usuario.html')
    
def crea_usu(request):
    return render(request,'app/crea_usu.html')

def comprado(request):
    carrito = Items_carrito.objects.all()
    carrito.delete()

    return render(request,'app/comprado.html')

