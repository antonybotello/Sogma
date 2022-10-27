# Generated by Django 4.1.1 on 2022-10-25 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionActivos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generarruta',
            name='fkPasajero',
        ),
        migrations.CreateModel(
            name='DetalleRuta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkPasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActivos.pasajero', verbose_name='Pasajero')),
                ('fkRuta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActivos.generarruta', verbose_name='Ruta')),
            ],
        ),
    ]
