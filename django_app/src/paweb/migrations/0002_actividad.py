# Generated by Django 4.1.1 on 2022-09-14 01:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('paweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fh_creado', models.DateTimeField(default=django.utils.timezone.now)),
                ('titulo', models.CharField(max_length=200)),
                ('hashtags', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('estilo', models.CharField(max_length=200)),
            ],
        ),
    ]