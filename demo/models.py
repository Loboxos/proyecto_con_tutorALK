from django.db import models
#los modelos son clases y estas clases se convierten en tablas de base d datos
#por un comando generamos las migraciones apartir de un modelo y las migraciones
#guardan la info de como deben ser creado las tablas y los atributos de la bd

class Marca(models.Model):
    #aqui no se hace esto def __init__(self)
    nombre=models.CharField(max_length=30,)#(unique=True)#unique es para q no se repita nombres
    #asi como unique tenemos tambien nonulo para no crear un campo con atributos nulos
    
    descripcion=models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id}- - -{self.nombre}"

class Producto(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField(default=0 )
    marca=models.ForeignKey(
    Marca,
    related_name="productos",
    on_delete=models.CASCADE)
    
    activo=models.BooleanField(default=True)

    def __str__(self):
        return self.nombre    
    
#si el framework tiene ORM nos da una interfaz mas facil para consultas sql 
#si hay que agregar un nuevo campo desde aca no de la bd
#en programas complejos es mejor las consultas normales de sql a orm