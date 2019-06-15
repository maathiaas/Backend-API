# Generated by Django 2.2.2 on 2019-06-14 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0003_espacialista_examen_tipoexamen'),
    ]

    operations = [
        migrations.AddField(
            model_name='examen',
            name='espacialista',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hospital.Espacialista'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='examen',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Paciente'),
        ),
    ]
