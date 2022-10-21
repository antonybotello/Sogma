# Generated by Django 4.1.1 on 2022-10-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0002_remove_activoequipooficina_estado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activoextintor',
            name='estado',
            field=models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, verbose_name='Estado'),
        ),
    ]