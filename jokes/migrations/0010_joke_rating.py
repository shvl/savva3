# Generated by Django 2.1.2 on 2018-12-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jokes', '0009_auto_20181118_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='joke',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]