# Generated by Django 2.2.12 on 2020-08-29 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakiye', '0014_auto_20200829_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kupon',
            name='kupon',
            field=models.CharField(max_length=120, verbose_name='Kuponunuzu Giriniz'),
        ),
    ]
