# Generated by Django 4.2.4 on 2023-09-01 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('size', '0001_initial'),
        ('store', '0004_product_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='size.produt_size'),
        ),
    ]
