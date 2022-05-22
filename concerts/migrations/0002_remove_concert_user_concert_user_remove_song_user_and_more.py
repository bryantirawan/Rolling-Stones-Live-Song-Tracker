# Generated by Django 4.0.4 on 2022-05-20 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('concerts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concert',
            name='user',
        ),
        migrations.AddField(
            model_name='concert',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='concerts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='song',
            name='user',
        ),
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to=settings.AUTH_USER_MODEL),
        ),
    ]