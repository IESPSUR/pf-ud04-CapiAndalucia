# Generated by Django 4.1.3 on 2022-11-12 14:36

from django.db import migrations, models
import django.db.models.deletion
import tienda.validations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('detalles', models.CharField(max_length=50, null=True, validators=[tienda.validations.validar_Textos], verbose_name='Detalles')),
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
                ('nombre_usuario', models.CharField(max_length=50, verbose_name='Nombre Usuario')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.productos')),
            ],
        ),
    ]
