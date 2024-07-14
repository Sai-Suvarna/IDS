# Generated by Django 5.0.6 on 2024-07-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0025_remove_batch_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placement',
            name='quantity',
        ),
        migrations.AddField(
            model_name='batch',
            name='quantity',
            field=models.CharField(default=1),
        ),
    ]