# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from core.models import TimeStampedModel
from reception.models import Patient
from staff.models import Doctor

# project imports
class Medicine(TimeStampedModel):
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=0, unique=True)
    description = models.TextField()
    supplier = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class MedPrice(TimeStampedModel):
#     date = models.DateTimeField()
#     medicine = models.ForeignKey(Medicine)
#     price = models.IntegerField()
#
#     def __str__(self):
#         return medicine.name
#
#     class Meta:
#         verbose_name_plural = 'Medicine Prices'


class Prescription(TimeStampedModel):
    doctor = models.ForeignKey(Doctor, related_name='prescribing_doctors')
    patient = models.ForeignKey(Patient, related_name='prescribed_patients')
    drug = models.ForeignKey(Medicine, related_name='prescribed_drugs')
    description = models.CharField(max_length=500)
    dosage = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    instructions = models.CharField(max_length=500)

    @property
    def charges(self):
        pass

    def __str__(self):
        return '{}-{}-{}'.format(self.doctor, self.patient, self.drug)
