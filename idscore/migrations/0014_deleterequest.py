# Generated by Django 5.0.6 on 2024-07-12 07:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idscore', '0013_alter_inventory_invreorderpoint'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeleteRequest',
            fields=[
                ('deleteId', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=255)),
                ('approverId', models.IntegerField()),
                ('createdtime', models.DateTimeField(auto_now_add=True)),
                ('modifiedtime', models.DateTimeField(auto_now=True)),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='idscore.product')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
