# Generated by Django 5.0.6 on 2024-06-21 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_num', models.CharField(max_length=15, unique=True)),
                ('designation', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('business_unit', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
