# Generated by Django 5.0.6 on 2024-07-12 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0027_alter_batch_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='quantity',
        ),
        migrations.AddField(
            model_name='placement',
            name='quantity',
            field=models.CharField(default=1),
        ),
    ]
