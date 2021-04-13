# Generated by Django 2.2.19 on 2021-04-13 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210413_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='cargo_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='main.CargoType'),
        ),
        migrations.AlterField(
            model_name='applicationform',
            name='cargo_weight',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='main.CargoWeight'),
        ),
    ]
