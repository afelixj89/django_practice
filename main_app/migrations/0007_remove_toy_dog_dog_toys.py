# Generated by Django 5.0.3 on 2024-04-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_toy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toy',
            name='dog',
        ),
        migrations.AddField(
            model_name='dog',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]
