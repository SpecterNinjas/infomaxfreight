# Generated by Django 2.2.19 on 2021-04-12 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_aboutus_aboutussection_statistics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField(max_length=4000)),
            ],
            options={
                'verbose_name': 'Careers',
                'verbose_name_plural': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=32)),
                ('email', models.EmailField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('message', models.TextField(max_length=2000)),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Insights',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('content', models.TextField(max_length=4000)),
                ('subcontent', models.TextField(max_length=2048)),
                ('image', models.ImageField(upload_to='main/insights/')),
            ],
            options={
                'verbose_name': 'Insights',
                'verbose_name_plural': 'Insights',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=16)),
                ('job_title', models.CharField(max_length=32)),
                ('twitter', models.URLField(max_length=32)),
                ('facebook', models.URLField(max_length=32)),
                ('telegram', models.URLField(max_length=32)),
                ('instagram', models.URLField(max_length=32)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team Members',
            },
        ),
        migrations.AlterField(
            model_name='carriersform',
            name='company',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='carriersform',
            name='email',
            field=models.EmailField(max_length=32),
        ),
        migrations.AlterField(
            model_name='carriersform',
            name='from_city',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='carriersform',
            name='fullname',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='carriersform',
            name='to_city',
            field=models.CharField(max_length=32),
        ),
        migrations.CreateModel(
            name='RequestQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=32)),
                ('company', models.CharField(max_length=32)),
                ('pickup_date', models.DateField(default=datetime.date.today)),
                ('delivery_date', models.DateField(default=datetime.date.today)),
                ('from_city', models.CharField(max_length=64)),
                ('to_city', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=32)),
                ('comments', models.TextField(max_length=3000)),
                ('truck_type', models.ForeignKey(on_delete=True, to='main.TruckType')),
                ('truckload_type', models.ForeignKey(on_delete=True, to='main.TruckloadType')),
            ],
            options={
                'verbose_name': 'Request Quote',
                'verbose_name_plural': 'Request Quotes',
            },
        ),
    ]
