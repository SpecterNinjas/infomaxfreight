# Generated by Django 2.2.19 on 2021-04-15 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_requestquote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonsbar',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
