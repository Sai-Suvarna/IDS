# Generated by Django 5.0.6 on 2024-07-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0010_rename_catreorderpoint_inventory_invreorderpoint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='expirydate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='batch',
            name='manufacturedate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
