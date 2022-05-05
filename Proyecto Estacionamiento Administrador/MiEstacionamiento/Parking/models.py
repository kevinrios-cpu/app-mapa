# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import geocoder

mapbox_token = 'pk.eyJ1Ijoid2F6b3dza2lkZXZlbG9wIiwiYSI6ImNrcTdneXZ4ejA2M2Uyd3VoY29hZTVjYXYifQ.wUjItHT_F5ZCMXUcwx5_xA'

class Admin(models.Model):
    id_emp = models.IntegerField(primary_key=True)
    nom_emp = models.CharField(max_length=25)
    apellido_emp = models.CharField(max_length=25)
    telefono = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'admin'


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    nom_ciudad = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ciudad'

    def __str__(self):
        return f'{self.nom_ciudad}'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nom_comuna = models.CharField(max_length=50)
    ciudad_id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'

    def __str__(self):
        return f'{self.nom_comuna}'


class DetalleHorario(models.Model):
    id_hor_det = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    hora_desde = models.DateField()
    hora_hasta = models.DateField()

    class Meta:
        managed = False
        db_table = 'detalle_horario'


class Direccion(models.Model):
    lugar = models.CharField(primary_key=True, max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.lugar, key=mapbox_token)
        g = g.latlng  # returns => [lat, long]
        self.latitud = g[0]
        self.longitud = g[1]
        return super(Direccion, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.lugar

    class Meta:
        managed = False
        db_table = 'direccion'


class Duenno(models.Model):
    rut_duenno = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    pnombre = models.CharField(max_length=30)
    snombre = models.CharField(max_length=30, blank=True, null=True)
    apaterno = models.CharField(max_length=30)
    amaterno = models.CharField(max_length=30)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dueño'
    
    def __str__(self):
        return f'{self.pnombre},{self.rut_duenno}'


class Horario(models.Model):
    id_horario = models.CharField(primary_key=True, max_length=20)
    puesto_id_puesto = models.ForeignKey('Puesto', models.DO_NOTHING, db_column='puesto_id_puesto')
    det_hor_id_hor_det = models.ForeignKey(DetalleHorario, models.DO_NOTHING, db_column='det_hor_id_hor_det')

    class Meta:
        managed = False
        db_table = 'horario'
        unique_together = (('id_horario', 'puesto_id_puesto', 'det_hor_id_hor_det'),)


class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nom_marca = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'marca'

    def __str__(self):
        return f'{self.nom_marca}'


class Modelo(models.Model):
    id_modelo = models.IntegerField(primary_key=True)
    nom_modelo = models.CharField(max_length=50)
    annio = models.IntegerField()
    marca_id_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='marca_id_marca')

    class Meta:
        managed = False
        db_table = 'modelo'
        unique_together = (('id_modelo', 'marca_id_marca'),)
    
    def __str__(self):
        return f'{self.nom_modelo}'


class Puesto(models.Model):
    id_puesto = models.IntegerField(primary_key=True)
    letra_puesto = models.CharField(max_length=2)
    num_puesto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'puesto'


class Reserva(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    usr_vehiculo_pat = models.ForeignKey('Usuario', models.DO_NOTHING,related_name='patente', db_column='usr_vehiculo_pat')
    usuario_rut_user = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usuario_rut_user')
    dia_reserva = models.IntegerField()
    sucursal_est = models.ForeignKey('SucursalEst', models.DO_NOTHING)
    horar_id_hor = models.ForeignKey(Horario, models.DO_NOTHING, db_column='horar_id_hor')
    horar_pue_id_puesto = models.ForeignKey(Horario, models.DO_NOTHING,related_name='id_puesto' ,db_column='horar_pue_id_puesto')
    horar_det_hor_id_hor_det = models.ForeignKey(Horario, models.DO_NOTHING, related_name='horario_det_id',db_column='horar_det_hor_id_hor_det')

    class Meta:
        managed = False
        db_table = 'reserva'


class SucursalEst(models.Model):
    id = models.IntegerField(primary_key=True)
    direccion_lugar = models.OneToOneField(Direccion, models.DO_NOTHING, db_column='direccion_lugar')
    nom_sucursal = models.CharField(max_length=30)
    fono_suc = models.IntegerField()
    admin_id_adm = models.ForeignKey(Admin, models.DO_NOTHING, db_column='admin_id_adm')

    class Meta:
        managed = False
        db_table = 'sucursal_est'

    def __str__(self):
        return f'{self.nom_sucursal}'


class Usuario(models.Model):
    rut_user = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    vehiculo_patente = models.ForeignKey('Vehiculo', models.DO_NOTHING, db_column='vehiculo_patente')
    comuna_id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='comuna_id_comuna')
    pnombre = models.CharField(max_length=30)
    snombre = models.CharField(max_length=30, blank=True, null=True)
    apaterno = models.CharField(max_length=30)
    amaterno = models.CharField(max_length=30)
    gmail = models.CharField(max_length=45)
    telefono = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        unique_together = (('rut_user', 'vehiculo_patente'),)

    def __str__(self):
        return f'{self.pnombre},{self.apaterno},{self.vehiculo_patente},{self.rut_user}'


class Vehiculo(models.Model):
    patente = models.CharField(primary_key=True, max_length=8)
    modelo_id_modelo = models.ForeignKey(Modelo, models.DO_NOTHING, db_column='modelo_id_modelo')
    modelo_marca_id_marca = models.ForeignKey(Modelo, models.DO_NOTHING,related_name='id_marca', db_column='modelo_marca_id_marca')
    duenno_rut_duenno = models.ForeignKey(Duenno, models.DO_NOTHING, related_name='rut_dueño',db_column='dueño_rut_dueño')
    color = models.CharField(max_length=25)
    num_ruedas = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'vehiculo'

    def __str__(self):
        return f'{self.patente}'
    
    def get_absolute_url(self):
        pass
