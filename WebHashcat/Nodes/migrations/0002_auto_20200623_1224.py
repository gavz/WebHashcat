# Generated by Django 3.0.7 on 2020-06-23 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nodes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='hostname',
            field=models.CharField(max_length=255),
        ),
    ]
