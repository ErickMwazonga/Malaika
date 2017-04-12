# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from malaika.models import PersonDetails

# Create your models here.
class Doctor(PersonDetails):
    SPECIALIZATION_CHOICES = {
        ('General','General'),
        ('Dentist','Dentist'),
        ('Physiotherapy','Physiotherapy'),
        ('Pharmacy','Pharmacy'),
    }
    specialization = models.CharField(max_length=200, choices=SPECIALIZATION_CHOICES)

    def __str__(self):
        return '{}-{}'.format(self.first_name,self.last_name)
