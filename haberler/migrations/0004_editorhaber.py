# Generated by Django 2.2.12 on 2020-08-28 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('haberler', '0003_auto_20200826_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='editorhaber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('haber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='haberler.Haberler')),
            ],
        ),
    ]
