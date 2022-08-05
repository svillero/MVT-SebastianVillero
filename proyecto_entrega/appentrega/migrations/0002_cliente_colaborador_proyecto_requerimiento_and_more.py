# Generated by Django 4.0.6 on 2022-08-04 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appentrega', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_id', models.IntegerField()),
                ('razon_social', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Colaborador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_alta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('pm_asignado', models.CharField(max_length=50)),
                ('fecha_alta', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('costo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('solicitud', models.CharField(max_length=100)),
                ('fecha_alta', models.DateField()),
                ('fecha_cierre', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Familiar',
        ),
    ]
