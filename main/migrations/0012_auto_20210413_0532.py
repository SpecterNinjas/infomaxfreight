# Generated by Django 2.2.19 on 2021-04-13 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_applicationform_fake'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestquote',
            name='truck_type',
        ),
        migrations.RemoveField(
            model_name='requestquote',
            name='truckload_type',
        ),
        migrations.RemoveField(
            model_name='shippersform',
            name='cargo_type',
        ),
        migrations.RemoveField(
            model_name='shippersform',
            name='cargo_weight',
        ),
        migrations.RemoveField(
            model_name='shippersform',
            name='truck_type',
        ),
        migrations.RemoveField(
            model_name='shippersform',
            name='truckload_type',
        ),
        migrations.DeleteModel(
            name='CarriersForm',
        ),
        migrations.DeleteModel(
            name='RequestQuote',
        ),
        migrations.DeleteModel(
            name='ShippersForm',
        ),
    ]
