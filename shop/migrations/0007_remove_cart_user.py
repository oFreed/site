# Generated by Django 3.1.7 on 2021-03-21 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]