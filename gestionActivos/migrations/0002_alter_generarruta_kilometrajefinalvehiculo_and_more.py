# Generated by Django 4.1.1 on 2022-10-15 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionActivos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generarruta',
            name='kilometrajeFinalVehiculo',
            field=models.IntegerField(verbose_name='Kilometraje Final'),
        ),
        migrations.AlterField(
            model_name='registrarmantenimiento',
            name='kilometrajeMantenimiento',
            field=models.IntegerField(verbose_name='Kilometraje del Vehículo'),
        ),
        migrations.AlterField(
            model_name='registrarmantenimiento',
            name='valorMantenimiento',
            field=models.IntegerField(verbose_name='Valor del Mantenimiento'),
        ),
    ]