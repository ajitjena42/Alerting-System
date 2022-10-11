# Generated by Django 3.0.2 on 2021-05-23 06:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('addDate', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('doctorname', models.CharField(max_length=100)),
                ('doctorqualification', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.IntegerField(default=0)),
                ('disease', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date.today)),
                ('clinicID', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cure', models.TextField()),
                ('precautions', models.TextField()),
                ('symptoms', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('pincode', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('addDate', models.DateField(default=datetime.date.today)),
                ('clinicID', models.CharField(max_length=30)),
            ],
        ),
    ]