# Generated by Django 5.0.6 on 2024-07-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0029_alter_placement_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='quantity',
            field=models.CharField(default=1),
        ),
    ]
