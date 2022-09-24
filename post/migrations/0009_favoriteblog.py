# Generated by Django 3.0.3 on 2020-03-18 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0008_auto_20200229_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_blog', to='post.Post')),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorite_blog', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]