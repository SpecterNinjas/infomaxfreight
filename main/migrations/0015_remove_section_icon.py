# Generated by Django 2.2.19 on 2021-04-13 00:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210413_0545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='icon',
        ),
    ]
