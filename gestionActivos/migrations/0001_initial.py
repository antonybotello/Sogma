# Generated by Django 4.1.1 on 2022-10-15 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('activos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaMantenimiento', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha del Mantenimiento')),
                ('lugarMantenimiento', models.CharField(max_length=50, verbose_name='Lugar del Mantenimiento')),
                ('ciudadMantenimiento', models.CharField(max_length=20, verbose_name='Lugar del Mantenimiento')),
                ('kilometrajeMantenimiento', models.IntegerField(max_length=20, verbose_name='Kilometraje del Vehículo')),
                ('numeroFactura', models.CharField(max_length=10, verbose_name='Número de Factura')),
                ('valorMantenimiento', models.IntegerField(max_length=10, verbose_name='Valor del Mantenimiento')),
                ('descripcionMantenimiento', models.TextField(max_length=200, verbose_name='Descripción')),
                ('fkIdEquipoOficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activoequipooficina', verbose_name='Equipo de Oficina')),
                ('fkIdExtintor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activoextintor', verbose_name='Extintor')),
                ('fkVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activovehiculo', verbose_name='Vehículo')),
            ],
        ),
        migrations.CreateModel(
            name='GenerarRuta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaSalida', models.TimeField(help_text='HH:MM', verbose_name='Hora de Salida')),
                ('horaRegreso', models.TimeField(help_text='HH:MM', verbose_name='Hora de Regreso')),
                ('fechaSalida', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha de Salida')),
                ('fechaRegreso', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha de Regreso')),
                ('lugarSalida', models.CharField(max_length=50, verbose_name='Lugar de Salida')),
                ('lugarDestino', models.CharField(max_length=50, verbose_name='Lugar de Destino')),
                ('kilometrajeFinalVehiculo', models.IntegerField(max_length=20, verbose_name='Kilometraje Final')),
                ('descripcionRuta', models.TextField(max_length=100, verbose_name='Descripción')),
                ('observacionesRuta', models.TextField(max_length=100, verbose_name='Observaciones')),
                ('fkPasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.pasajero', verbose_name='Pasajero')),
                ('fkUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario', verbose_name='Usuario')),
                ('fkVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activovehiculo', verbose_name='Vehículo')),
            ],
        ),
        migrations.CreateModel(
            name='GenerarAlarma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaMantenimiento', models.DateField(help_text='MM/DD/AAAA', verbose_name='Fecha Mantenimiento')),
                ('tipoMantenimiento', models.CharField(choices=[('Periodico', 'Periodico'), ('Preventivo', 'Preventivo'), ('Kilometraje', 'Kilometraje')], default='Preventivo', max_length=15, verbose_name='Tipo de Mantenimiento')),
                ('descripcionMantenimiento', models.TextField(max_length=100, verbose_name='Descripción del Mantenimiento')),
                ('fkIdEquipoOficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activoequipooficina', verbose_name='Equipo de Oficina')),
                ('fkIdExtintor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activoextintor', verbose_name='Extintor')),
                ('fkVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activovehiculo', verbose_name='Vehículo')),
            ],
        ),
    ]
