# Generated by Django 4.1.1 on 2022-11-01 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0007_alter_activovehiculo_fechafinsoat_and_more'),
        ('gestionActivos', '0003_alter_generarruta_descripcionruta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrarmantenimiento',
            name='fkIdEquipoOficina',
        ),
        migrations.RemoveField(
            model_name='registrarmantenimiento',
            name='fkIdExtintor',
        ),
        migrations.RemoveField(
            model_name='registrarmantenimiento',
            name='fkVehiculo',
        ),
        migrations.RemoveField(
            model_name='registrarmantenimiento',
            name='kilometrajeMantenimiento',
        ),
        migrations.CreateModel(
            name='MantenimientoVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kilometrajeMantenimiento', models.IntegerField(verbose_name='Kilometraje del Vehículo')),
                ('fkRegistrarMantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActivos.registrarmantenimiento', verbose_name='mantenimiento')),
                ('fkVehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activovehiculo', verbose_name='Vehículo')),
            ],
        ),
        migrations.CreateModel(
            name='MantenimientoExtintor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkIdExtintor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activoextintor', verbose_name='Extintor')),
                ('fkRegistrarMantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActivos.registrarmantenimiento', verbose_name='mantenimiento')),
            ],
        ),
        migrations.CreateModel(
            name='MantenimientoEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fkIdEquipoOficina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activos.activoequipooficina', verbose_name='Equipo de Oficina')),
                ('fkRegistrarMantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionActivos.registrarmantenimiento', verbose_name='mantenimiento')),
            ],
        ),
    ]