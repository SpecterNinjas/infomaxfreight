# Generated by Django 2.2.19 on 2021-04-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210413_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to='main/section/'),
        ),
    ]
