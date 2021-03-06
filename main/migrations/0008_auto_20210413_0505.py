# Generated by Django 2.2.19 on 2021-04-13 00:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_faq_footer_privacypolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Application Category',
                'verbose_name_plural': 'Application Categories ',
            },
        ),
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=128)),
                ('pickup_date', models.DateField(default=datetime.date.today)),
                ('delivery_date', models.DateField(default=datetime.date.today)),
                ('from_city', models.CharField(max_length=128)),
                ('to_city', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=64)),
                ('comments', models.TextField(max_length=3000)),
                ('cargo_type', models.ForeignKey(on_delete=True, to='main.CargoType')),
                ('cargo_weight', models.ForeignKey(on_delete=True, to='main.CargoWeight')),
                ('category', models.ForeignKey(on_delete=True, to='main.ApplicationCategory', verbose_name='Категория форма')),
            ],
            options={
                'verbose_name': 'Application Form',
                'verbose_name_plural': 'Applications Form',
            },
        ),
        migrations.CreateModel(
            name='CarriesApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=3000)),
                ('image', models.ImageField(upload_to='main/subcarriers/')),
                ('url', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'SubCarrier',
                'verbose_name_plural': 'SubCarriers',
            },
        ),
        migrations.DeleteModel(
            name='SubCarriers',
        ),
        migrations.RenameField(
            model_name='anonsbar',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='section',
            old_name='logo',
            new_name='icon',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='logo',
            new_name='icon',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='content',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='header',
        ),
        migrations.RemoveField(
            model_name='slider',
            name='is_active',
        ),
        migrations.AddField(
            model_name='slider',
            name='description',
            field=models.TextField(default=1, max_length=1024, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Draft'),
        ),
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(default=1, max_length=512, verbose_name='Наимование'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anonsbar',
            name='url',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carriers',
            name='title',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='services',
            name='url',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='main/slider/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.SlugField(blank=True, null=True, verbose_name='Url'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='fake',
            field=models.ForeignKey(on_delete=True, to='main.Carriers'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='truck_type',
            field=models.ForeignKey(on_delete=True, to='main.TruckType'),
        ),
        migrations.AddField(
            model_name='applicationform',
            name='truckload_type',
            field=models.ForeignKey(on_delete=True, to='main.TruckloadType'),
        ),
    ]
