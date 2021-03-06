# Generated by Django 2.1.2 on 2018-11-17 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20181117_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theorem',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Resource')),
                ('text', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('base.resource',),
        ),
    ]
