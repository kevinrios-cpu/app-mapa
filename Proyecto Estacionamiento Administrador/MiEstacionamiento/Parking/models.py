# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from pyexpat import model
from django.db import models
from django.forms import PasswordInput
import geocoder
from django.urls import reverse
mapbox_token = 'pk.eyJ1Ijoid2F6b3dza2lkZXZlbG9wIiwiYSI6ImNrcTdneXZ4ejA2M2Uyd3VoY29hZTVjYXYifQ.wUjItHT_F5ZCMXUcwx5_xA'

class Admin(models.Model):
    id_emp = models.IntegerField(primary_key=True)
    nom_emp = models.CharField(max_length=25)
    apellido_emp = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.id_emp}'


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    nom_ciudad = models.CharField(max_length=40)



    def __str__(self):
        return f'{self.nom_ciudad}'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=50)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    def __str__(self):

        return f'{self.nom_comuna}'
        
class Direccion(models.Model):
    lugar = models.CharField(max_length=100)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.lugar, key=mapbox_token)
        g = g.latlng  # returns => [lat, long]
        self.latitud = g[0]
        self.longitud = g[1]
        return super(Direccion, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.lugar


class Duenno(models.Model):
    rut_duenno = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=30)
    snombre = models.CharField(max_length=30, blank=True, null=True)
    apaterno = models.CharField(max_length=30)
    amaterno = models.CharField(max_length=30)
    telefono = models.IntegerField(blank=True, null=True)


    
    def __str__(self):
        return f'{self.pnombre},{self.rut_duenno}'












class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nom_marca = models.CharField(max_length=40)


    def __str__(self):
        return f'{self.nom_marca}'


class Modelo(models.Model):
    id_modelo = models.IntegerField(primary_key=True)
    nom_modelo = models.CharField(max_length=50)
    annio = models.IntegerField()
    marca_id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='marca_id_marca')

    class Meta:

        unique_together = (('id_modelo', 'marca_id_marca'),)
    
    def __str__(self):
        return f'{self.nom_modelo}'


class Puesto(models.Model):
    id_puesto = models.IntegerField(primary_key=True)
    letra_puesto = models.CharField(max_length=2)
    num_puesto = models.IntegerField()
    sucursal_est = models.ForeignKey('SucursalEst', models.DO_NOTHING)

    def __str__(self):
        return f'{self.id_puesto},{self.letra_puesto}{self.num_puesto}'

class Reserva(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING,related_name='patente', db_column='usr_vehiculo_pat')
    fecha = models.DateField()
    hora_desde = models.TimeField()
    hora_hasta = models.TimeField()
    estacionamiento = models.ForeignKey('Puesto', models.DO_NOTHING)


    
    def __str__(self):
        return f'{self.id_reserva},{self.usuario}'

    def get_absolute_url(self):
        
        return reverse('reserva_detail', args=[str(self.id_reserva)])

class SucursalEst(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion_lugar = models.OneToOneField(Direccion, models.DO_NOTHING, db_column='direccion_lugar')
    nom_sucursal = models.CharField(max_length=30)
    fono_suc = models.IntegerField()
    admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='admin_id_adm')



    def __str__(self):
        return f'{self.nom_sucursal}'
    
    def get_absolute_url(self):
        
        return reverse('usuario_detail', args=[str(self.id)])


class Usuario(models.Model):
    rut_user = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nom_user = models.CharField(max_length=30, null=False)
    password = models.CharField(max_length=30,  null=False)
    vehiculo_patente = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente')
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    pnombre = models.CharField(max_length=30, null=False)
    snombre = models.CharField(max_length=30, blank=True, null=True)
    apaterno = models.CharField(max_length=30, null=False)
    amaterno = models.CharField(max_length=30, null=False)
    gmail = models.CharField(max_length=45, null=False)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:

        unique_together = (('rut_user', 'vehiculo_patente'),)

    def __str__(self):
        return f'{self.pnombre},{self.apaterno},{self.vehiculo_patente},{self.rut_user}'
    
    def get_absolute_url(self):
        
        return reverse('usuario_detail', args=[str(self.rut_user)])


class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=8)
    modelo = models.ForeignKey(Modelo, models.DO_NOTHING, db_column='modelo_id_modelo')
    marca = models.ForeignKey(Marca, models.DO_NOTHING, default=1)
    duenno = models.ForeignKey(Duenno, models.DO_NOTHING, related_name='rut_dueño',db_column='dueño_rut_dueño')
    color = models.CharField(max_length=25)
    num_ruedas = models.BooleanField()



    def __str__(self):
        return f'{self.patente}'
    
    def get_absolute_url(self):
        pass
