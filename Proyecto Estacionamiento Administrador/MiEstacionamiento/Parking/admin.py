from ast import Mod
from django.contrib import admin
from .models import Admin,Usuario,Vehiculo,Ciudad,Comuna,DetalleHorario,Direccion,Duenno,Horario,Marca,Modelo,Puesto,Reserva,SucursalEst


admin.site.register(Admin)
admin.site.register(Usuario)
admin.site.register(Vehiculo)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(DetalleHorario)
admin.site.register(Direccion)
admin.site.register(Duenno)
admin.site.register(Horario)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Puesto)
admin.site.register(Reserva)
admin.site.register(SucursalEst)