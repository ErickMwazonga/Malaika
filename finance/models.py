# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from reception.models import Patient
from operations.models import Treatment

# Create your models here.
class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    charges = models.CharField(max_length=200, default=0)

    def __str__(self):
        return '{}-{}'.format(self.patient, self.charges)
