from email.policy import default
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django.contrib import admin

from .models import Trabajador, Categoria, Producto, Produccion


# Register your models here.
@admin.register(Trabajador) #decorador personalizado
class TrabajadorAdmin(admin.ModelAdmin):  #metodo para personalizar 
    list_display = ('id','cedula','nombre','apellido','correo','nombreCompleto')# vista de los elementos en columnas
    search_fields = ['nombre','cedula'] # añade un buscador para buscar por el campo seleccionado

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display =('nombre', 'ficha_tecnica', 'costo', 'categoria', 'color','descripcionCategoria' )
    search_fields = ['nombre','categoria__nombre'] #de este modo se dice porque componente de categoria se desa buscar
    list_filter = ['categoria','color'] # añade un filtro por el elemento seleccionado
    list_editable = ['color','categoria'] # permite editar los campos en directo, se recomienda no dejarla activa siempre por seguridad

    def descripcionCategoria(self, obj): # se utiliza este metodo para llamar un elemento de la otra tabla
        return obj.categoria.desc

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'desc')
    

@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'producto', 'cantidad', 'fecha_creacion')
    

