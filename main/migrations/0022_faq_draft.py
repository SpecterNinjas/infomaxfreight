# Generated by Django 2.2.19 on 2021-04-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20210413_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
