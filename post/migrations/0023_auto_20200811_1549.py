# Generated by Django 2.2.12 on 2020-08-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_userprofile_bakiye'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bakiye',
            field=models.IntegerField(blank=True, max_length=1000, null=True, verbose_name='bakiye'),
        ),
    ]
