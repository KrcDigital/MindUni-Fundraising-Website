# Generated by Django 2.2.12 on 2020-08-11 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakiye', '0004_auto_20200811_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kupon',
            name='kod',
            field=models.CharField(default=1, max_length=120, verbose_name='Kodunuzu Giriniz'),
            preserve_default=False,
        ),
    ]
