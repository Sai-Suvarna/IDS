# Generated by Django 5.0.6 on 2024-07-12 16:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0022_placement_batchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placement',
            name='batchid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idscore.batch'),
        ),
    ]