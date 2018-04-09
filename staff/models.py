# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from core.models import TimeStampedModel
from hospital.models import Person


# Create your models here.
class DoctorSpeciality(TimeStampedModel):
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.specialty

    class Meta:
        verbose_name = 'Doctor specialty'
        verbose_name_plural = 'Doctors specialties'


class Doctor(Person):
    person = models.OneToOneField(User, related_name='doctors')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    specialty = models.ManyToManyField(DoctorSpeciality)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class NurseSpeciality(TimeStampedModel):
    specialty = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.specialty

    class Meta:
        verbose_name = 'Nurse specialty'
        verbose_name_plural = 'Nurse specialties'


class Nurse(TimeStampedModel):
    person = models.OneToOneField(User, related_name='nurses')
    specialty = models.ManyToManyField(NurseSpeciality)

    def __str__(self):
        return self.specialty
