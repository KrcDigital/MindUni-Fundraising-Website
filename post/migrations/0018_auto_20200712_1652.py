# Generated by Django 3.0.7 on 2020-07-12 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_auto_20200712_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='category',
            name='keywords',
        ),
    ]
