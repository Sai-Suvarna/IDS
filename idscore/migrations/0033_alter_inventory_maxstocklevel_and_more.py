# Generated by Django 5.0.6 on 2024-07-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0032_rename_quantity_placement_placementquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='maxstocklevel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='minstocklevel',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
