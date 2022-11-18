# Generated by Django 4.1.2 on 2022-11-18 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tienda.validations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, validators=[tienda.validations.validar_Textos], verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, validators=[tienda.validations.validar_Textos], verbose_name='Nombre')),
                ('modelo', models.CharField(max_length=50, validators=[tienda.validations.validar_Textos], verbose_name='Modelo')),
                ('unidades', models.IntegerField(verbose_name='Unidades')),
                ('precio', models.FloatField(default=0, validators=[tienda.validations.validar_precio], verbose_name='Precio')),
                ('detalles', models.TextField(max_length=500, null=True, verbose_name='Detalles')),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('unidades', models.IntegerField(verbose_name='Unidades')),
                ('importe', models.CharField(max_length=50, validators=[tienda.validations.validar_Textos], verbose_name='Importe')),
                ('nombre_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.productos')),
            ],
        ),
    ]
