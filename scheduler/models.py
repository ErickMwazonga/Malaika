# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import TimeStampedModel
from reception.models import Patient
from staff.models import Doctor


class Appointment(TimeStampedModel):
    patient = models.ForeignKey(Patient, related_name='patient_appointments')
    doctor = models.ForeignKey(Doctor, related_name='patient_appointments')
    description = models.CharField(max_length=100)
    hospital = models.CharField(max_length=50, default='Malaika Hospital',
                                blank=True, null=True)

    def __str__(self):
        return '{}-{}'.format(self.patient, self.doctor)



class Notification(TimeStampedModel):
    type = models.CharField(max_length=50)
    date = models.CharField(max_length=100)
    user = models.CharField(max_length=50)
    doctor = models.CharField(max_length=50)
    data = models.CharField(max_length=200)
    data2 = models.CharField(max_length=200)


class Message(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date = models.CharField(max_length=50)
