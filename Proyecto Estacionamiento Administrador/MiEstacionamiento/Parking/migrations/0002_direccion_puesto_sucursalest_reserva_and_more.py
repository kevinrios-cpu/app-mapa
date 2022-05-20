# Generated by Django 4.0 on 2022-05-13 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=100)),
                ('latitud', models.FloatField(blank=True, null=True)),
                ('longitud', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puesto',
            fields=[
                ('id_puesto', models.IntegerField(primary_key=True, serialize=False)),
                ('letra_puesto', models.CharField(max_length=2)),
                ('num_puesto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SucursalEst',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_sucursal', models.CharField(max_length=30)),
                ('fono_suc', models.IntegerField()),
                ('admin', models.ForeignKey(db_column='admin_id_adm', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.admin')),
                ('direccion_lugar', models.OneToOneField(db_column='direccion_lugar', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('hora_desde', models.TimeField()),
                ('hora_hasta', models.TimeField()),
                ('estacionamiento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.puesto')),
                ('usuario', models.ForeignKey(db_column='usr_vehiculo_pat', on_delete=django.db.models.deletion.DO_NOTHING, related_name='patente', to='Parking.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='puesto',
            name='sucursal_est',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.sucursalest'),
        ),
    ]
