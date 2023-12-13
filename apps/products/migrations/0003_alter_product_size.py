# Generated by Django 4.2.6 on 2023-10-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_brand_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('BIG', 'big'), ('SMOL', 'small')], max_length=50, null=True),
        ),
    ]
