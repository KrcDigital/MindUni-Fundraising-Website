# Generated by Django 3.0.7 on 2020-06-28 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('takip', '0004_auto_20200628_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fallowing',
            options={'verbose_name_plural': 'Fallowing'},
        ),
        migrations.RemoveField(
            model_name='fallowing',
            name='fallower',
        ),
        migrations.AddField(
            model_name='fallowing',
            name='fallow',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fallow', to=settings.AUTH_USER_MODEL, verbose_name='Takip Eden Kullanıcı'),
        ),
    ]