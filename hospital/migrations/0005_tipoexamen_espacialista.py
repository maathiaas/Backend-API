# Generated by Django 2.2.2 on 2019-06-15 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_auto_20190614_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoexamen',
            name='espacialista',
            field=models.ForeignKey(default=222, on_delete=django.db.models.deletion.CASCADE, to='hospital.Espacialista'),
            preserve_default=False,
        ),
    ]
