from django.shortcuts import render
from demo.models import Producto
from django.http import JsonResponse
from django.forms.models import model_to_dict
# Create your views here.
def listado_productos(request):
    productos = list(Producto.objects.values())
    return JsonResponse(productos,safe=False)
def detalle_producto(request,id_producto):
    producto=Producto.objects.get(id=id_producto)
    producto_dict=model_to_dict(producto)
    return JsonResponse(producto_dict,safe=False)