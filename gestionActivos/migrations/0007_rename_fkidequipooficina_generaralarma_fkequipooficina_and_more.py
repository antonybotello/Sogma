# Generated by Django 4.1.1 on 2022-11-02 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionActivos', '0006_mantenimientoextintor_usado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generaralarma',
            old_name='fkIdEquipoOficina',
            new_name='fkEquipoOficina',
        ),
        migrations.RenameField(
            model_name='generaralarma',
            old_name='fkIdExtintor',
            new_name='fkExtintor',
        ),
        migrations.RenameField(
            model_name='mantenimientoequipo',
            old_name='fkIdEquipoOficina',
            new_name='fkEquipoOficina',
        ),
        migrations.RenameField(
            model_name='mantenimientoextintor',
            old_name='fkIdExtintor',
            new_name='fkExtintor',
        ),
    ]