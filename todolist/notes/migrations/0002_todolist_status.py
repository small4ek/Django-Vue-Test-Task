# Generated by Django 3.0.5 on 2020-04-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]