# Generated by Django 4.1.1 on 2022-10-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0003_activoextintor_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='activoequipooficina',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='activovehiculo',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado'),
        ),
    ]