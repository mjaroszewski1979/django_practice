# Generated by Django 4.0.3 on 2022-04-01 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
    ]
