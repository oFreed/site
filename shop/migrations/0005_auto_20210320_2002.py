# Generated by Django 3.1.7 on 2021-03-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20210320_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
        migrations.AddField(
            model_name='cart',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='cart',
            name='product_list',
            field=models.ManyToManyField(blank=True, to='shop.Product'),
        ),
    ]