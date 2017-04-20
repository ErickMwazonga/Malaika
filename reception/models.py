# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# project imports
from django.db import models
from malaika.models import PersonDetails, Room
from staff.models import Doctor
from malaika.models import Diagnose

from django.utils import timezone


class Patient(PersonDetails):
    contact_no = models.CharField(max_length=200)
    next_of_kin = models.CharField(max_length=200)

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)


class In_patient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_adm = models.DateField(default=timezone.now().date())
    date_of_discarge = models.DateField()
    diagnosis = models.ForeignKey(Diagnose, on_delete=None)
    doctor = models.ForeignKey(Doctor, on_delete=None)
    room = models.ForeignKey(Room, on_delete=None)

    def __str__(self):
        return '{}-{}'.format(self.patient, self.room)


class Out_patient(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now().date())
    diagnosis = models.ForeignKey(Diagnose, on_delete=None)
    doctor = models.ForeignKey(Doctor, on_delete=None)

    def __str__(self):
        return '{}'.format(self.patient)
