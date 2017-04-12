# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from reception.models import Patient
from staff.models import Doctor

from django.utils import timezone

# Create your models here.
class Diagnose(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=0, unique=True)
    description = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.code, self.name)


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=None)
    date = models.DateField(default=timezone.now().date())
    symptoms = models.TextField
    diagnosis = models.ForeignKey(Diagnose, on_delete=None)
    doctors_comments = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.patient, self.doctor, self.diagnosis)
