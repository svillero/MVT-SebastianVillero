# Generated by Django 4.0.6 on 2022-08-06 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appentrega', '0003_alter_proyecto_fecha_entrega_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='costo',
            field=models.IntegerField(default=1),
        ),
    ]
