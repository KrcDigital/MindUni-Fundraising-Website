# Generated by Django 2.2.12 on 2020-08-29 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_auto_20200811_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='kod',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='kod'),
        ),
    ]