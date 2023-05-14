
from django.shortcuts import render,HttpResponse,redirect
from demo.models import Producto,Marca


# Create your views here.
def ejemplo_template(request):
    listado_marcas = Marca.objects.all()

    context = {
        "nombre": "Maria",
        "apellido": "Torres",
        "edad": 38,
        "listado_marcas": listado_marcas
    }

    return render(
        request,
        "demo/ejemplo.html",
        context
    )
def saludar(request):
    return HttpResponse("Hola mundoo!!")
def saludar_con_nombre(request,nombre):
    return HttpResponse(f"HOLA {nombre}")#responde en html

def listado_productos(request):
    lista_productos=Producto.objects.all()
    context={
        "listado_productos":lista_productos
    }
    
    return render(request,"demo/listado_productos.html",context)
    
def nuevo_producto(request):
    lista_marcas = Marca.objects.all()

    context = {
        "listado_marcas": lista_marcas
    }

    if request.POST:
        nombre_producto = request.POST["nombre"]
        precio_producto = request.POST["precio"]
        marca_id = request.POST["marca"]

        # marca = Marca.objects.get(id=marca_id)

        Producto.objects.create(
            nombre=nombre_producto,
            precio=precio_producto,
            marca_id=marca_id
        )

    return render(
        request,
        "demo/nuevo_producto.html",
        context
    )

def modificar_producto(request,producto_id):
    lista_marcas = Marca.objects.all()
    producto=Producto.objects.get(id=producto_id)

    context = {
        "listado_marcas": lista_marcas,
        "producto":producto
    }
    if request.POST:
        nombre_producto = request.POST["nombre"]
        precio_producto = request.POST["precio"]
        marca_id = request.POST["marca"]
    
        producto.nombre=nombre_producto
        producto.precio=precio_producto
        producto.marca_id=marca_id

        producto.save()
    return render(
        request,
        "demo/modificar_producto.html",
        context
    )

def eliminar_producto(request,producto_id):
    try:
       producto = Producto.objects.get(id=producto_id)
       producto.delete()
    except:
        return HttpResponse("no se ha encontrado el producto a eliminar")
    #return HttpResponse("el producto ha sido eliminado")

    return redirect("listado_productos")
def desactivar_producto(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.activo=False
    producto.save()
    return redirect('listado_productos')

def activar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.activo=True
    producto.save()
    return redirect('listado_productos')

def home_page(request):
    return render(request, "demo/home_page.html")
#class Saludar(View):
    #codigo
    #si son clases entonces en demo/urls ponemos en path Saludar.as_view()
