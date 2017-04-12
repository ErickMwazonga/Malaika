# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils import timezone

class PersonDetails(models.Model):
    GENDER_CHOICES = {
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField(default=timezone.now().date())
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Room(models.Model):
    ROOM_TYPES = {
        ('General','General'),
        ('Maternity','Maternity'),
        ('Ward','Ward'),
    }
    room_number = models.IntegerField(default=0, unique=True)
    room_type = models.CharField(max_length=200, choices=ROOM_TYPES)

    def __str(self):
        return 'Room {}'.format(self.room_number)
