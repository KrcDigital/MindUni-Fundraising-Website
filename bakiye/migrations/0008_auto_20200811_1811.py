# Generated by Django 2.2.12 on 2020-08-11 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakiye', '0007_auto_20200811_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gonderiler2',
            name='category',
        ),
        migrations.RemoveField(
            model_name='gonderiler2',
            name='category2',
        ),
        migrations.RemoveField(
            model_name='gonderiler2',
            name='category3',
        ),
        migrations.RemoveField(
            model_name='gonderiler2',
            name='category4',
        ),
        migrations.RemoveField(
            model_name='gonderiler2',
            name='category5',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Category2',
        ),
        migrations.DeleteModel(
            name='Category3',
        ),
        migrations.DeleteModel(
            name='Category4',
        ),
        migrations.DeleteModel(
            name='Category5',
        ),
    ]
