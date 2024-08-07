# Generated by Django 5.0.6 on 2024-07-05 07:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='batchid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='batch',
            name='productid',
            field=models.ForeignKey(default=37, on_delete=django.db.models.deletion.CASCADE, to='idscore.product'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='quantity',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
