# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from core.models import TimeStampedModel
from hospital.models import Person


# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User Type'
        verbose_name_plural = 'User Types'


# def get_doctors():
#     doctor =  UserType.objects.get_or_create(name='Doctors', description='Doctors')
#     return doctor.id
#
# def get_nurses():
#     nurse = UserType.objects.get_or_create(name='Nurses', description='Nurses')
#     return nurse.id


class Speciality(TimeStampedModel):
    specialty = models.CharField(max_length=100)

    def __str__(self):
        return self.specialty

    class Meta:
        verbose_name = 'Specialty'
        verbose_name_plural = 'Specialties'


class Doctor(Person):
    person = models.OneToOneField(User, related_name='doctors')
    avatar = models.ImageField(upload_to='avatars/doctors', null=True, blank=True)
    specialty = models.ManyToManyField(Speciality)
    user_type = models.ForeignKey(UserType, related_name='doctors')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Nurse(Person):
    person = models.OneToOneField(User, related_name='nurses')
    avatar = models.ImageField(upload_to='avatars/nurses', null=True, blank=True)
    specialty = models.ManyToManyField(Speciality)
    user_type = models.ForeignKey(UserType, related_name='nurses')

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class OtherStaff(Person):
    person = models.OneToOneField(User)
    avatar = models.ImageField(upload_to='avatars/otherstaff', null=True, blank=True)
    specialty = models.ManyToManyField(Speciality)
    user_type = models.ForeignKey(UserType)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
