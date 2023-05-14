from django.contrib import admin

# Register your models here.
#usamos los modelos creados previamente p'ara construir automaticamente
#un area dentro del sistema q uso para crear consultar actualizar y borrrar registros

from django.contrib import admin

from demo.models import Marca,Producto

class MarcaAdmin(admin.ModelAdmin):
    model = Marca

    # muestra la info en columnas en el admin
    list_display = [
        "id",
        "nombre",
        "descripcion",
    ]

    # busqueda por fields
    search_fields = [
        "nombre",
        "descripcion",
    ]


class ProductoAdmin(admin.ModelAdmin):
    model = Producto
    list_display = [
        "id",
        "nombre",
        "precio",
        "marca",
    ]
    search_fields = [
        "nombre",
        "marca__nombre"
    ]

    # filtros: se despliega a la izquierda del admin
    list_filter = [
        "marca__nombre",
        "activo",
    ]

    # campos de solo lectura
    readonly_fields = [
        "precio",
        "activo"
    ]


# registrar modelos
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Producto, ProductoAdmin)