# Generated by Django 2.2.19 on 2021-04-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20210419_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carriersform',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
