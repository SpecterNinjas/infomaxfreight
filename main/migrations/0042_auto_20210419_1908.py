# Generated by Django 2.2.19 on 2021-04-19 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20210419_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anonsbar',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='carriesapplication',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='navbar',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='vacancies',
            name='url',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
