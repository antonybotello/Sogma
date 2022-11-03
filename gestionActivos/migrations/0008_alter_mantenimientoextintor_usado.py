# Generated by Django 4.1.1 on 2022-11-03 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionActivos', '0007_rename_fkidequipooficina_generaralarma_fkequipooficina_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mantenimientoextintor',
            name='usado',
            field=models.CharField(blank=True, choices=[('SI', 'SI'), ('NO', 'NO')], default='NO', max_length=5, verbose_name='¿Extintor usado?'),
        ),
    ]
