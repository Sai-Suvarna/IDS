# Generated by Django 5.0.6 on 2024-07-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0026_remove_placement_quantity_batch_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='quantity',
            field=models.CharField(),
        ),
    ]