# Generated by Django 2.2 on 2022-12-27 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20221217_1928'),
        ('cart', '0003_item_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='item',
            new_name='items',
        ),
    ]
