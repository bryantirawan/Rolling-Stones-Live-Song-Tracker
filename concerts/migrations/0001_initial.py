# Generated by Django 4.0.4 on 2022-05-19 20:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=200, null=True)),
                ('concertid', models.CharField(default='didnotsaveproperly', max_length=200)),
                ('date', models.DateField(null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('song', models.ManyToManyField(blank=True, null=True, to='concerts.song')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='concerts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]