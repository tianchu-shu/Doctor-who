# Generated by Django 2.0.2 on 2018-02-19 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waittimes', '0002_auto_20180218_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientwaittime',
            name='metro_area',
            field=models.FloatField(null=True),
        ),
    ]