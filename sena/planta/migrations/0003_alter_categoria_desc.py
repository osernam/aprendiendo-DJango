# Generated by Django 4.0.6 on 2022-08-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0002_categoria_producto_produccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='desc',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]