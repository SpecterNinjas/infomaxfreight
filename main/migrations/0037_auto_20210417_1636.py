# Generated by Django 2.2.19 on 2021-04-17 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20210417_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonsbar',
            name='url',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carriesapplication',
            name='url',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
