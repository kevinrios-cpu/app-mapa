# Generated by Django 4.0 on 2022-06-17 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Parking', '0002_direccion_puesto_sucursalest_reserva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sucursalest',
            name='direccion_lugar',
            field=models.ForeignKey(db_column='direccion_lugar', on_delete=django.db.models.deletion.DO_NOTHING, to='Parking.direccion'),
        ),
    ]