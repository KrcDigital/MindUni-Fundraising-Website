# Generated by Django 2.2.12 on 2020-08-29 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakiye', '0012_odemebilgi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kupon',
            name='kupon',
            field=models.IntegerField(max_length=120, verbose_name='Kuponunuzu Giriniz'),
        ),
    ]
