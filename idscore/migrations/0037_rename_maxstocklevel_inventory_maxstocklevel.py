# Generated by Django 5.0.6 on 2024-07-13 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0036_rename_batchid_batch_batchid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='maxstocklevel',
            new_name='maxStockLevel',
        ),
    ]
