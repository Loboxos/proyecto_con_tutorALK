from django.urls import path
from .views import listado_productos,detalle_producto

urlpatterns = [
    path("productos/",listado_productos,name="Listado_productos"),
    path("productos/<int:id_producto>",detalle_producto,name="detalle_producto")

]