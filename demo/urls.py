from django.urls import path

from .views import (saludar,
saludar_con_nombre,
ejemplo_template,
listado_productos,
nuevo_producto,
modificar_producto,
eliminar_producto,
desactivar_producto,
activar_producto,
home_page)

urlpatterns = [
    path("saludar/",saludar ,name="saludar"),
    path("saludar_con_nombre/<str:nombre>",saludar_con_nombre ,name="saludar_con_nombre"),
    path("ejemplo_template/",ejemplo_template ,name="ejemplo_template"),
    path("productos/listado_productos",listado_productos,name="listado_productos"),
    path("productos/nuevo",nuevo_producto,name="nuevo_producto"),
    path("productos/modificar/<int:producto_id>",modificar_producto,name="modificar_producto"),
    path("productos/eliminar/<int:producto_id>",eliminar_producto,name="eliminar_producto"),
    path("productos/desactivar/<int:producto_id>",desactivar_producto,name="desactivar_producto"),
    path("productos/activar/<int:producto_id>",activar_producto,name="activar_producto"),
    path("home_page/",home_page,name="home_page")
]