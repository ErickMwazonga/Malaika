# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-04-09 11:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('staff', models.ManyToManyField(related_name='_department_staff_+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('code', models.IntegerField(default=0, unique=True)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HospitalStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('totalAdmins', models.IntegerField()),
                ('totalDoctors', models.IntegerField()),
                ('totalNurses', models.IntegerField()),
                ('totalPatients', models.IntegerField()),
                ('successfulLogins', models.IntegerField()),
                ('failedLogins', models.IntegerField()),
                ('appointmentsCreated', models.IntegerField()),
                ('medicationsPrescribed', models.IntegerField()),
                ('testsConducted', models.IntegerField()),
                ('messagesSent', models.IntegerField()),
                ('notificationsReceived', models.IntegerField()),
                ('patientsAdmitted', models.IntegerField()),
                ('oldestUser', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Hospital Statistics',
                'verbose_name_plural': 'Hospital Statistics',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('room_number', models.IntegerField(blank=True, default=0)),
                ('departmnt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.Department')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Room type',
                'verbose_name_plural': 'Room types',
            },
        ),
        migrations.CreateModel(
            name='supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.RoomType'),
        ),
    ]
