# Generated by Django 2.2.12 on 2020-08-28 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='email',
        ),
    ]
