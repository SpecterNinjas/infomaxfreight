# Generated by Django 2.2.19 on 2021-04-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20210417_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='url',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
