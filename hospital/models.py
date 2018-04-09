# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from core.models import TimeStampedModel


class Person(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15, default=0)
    age = models.IntegerField(default=0)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    next_of_kin = models.CharField(max_length=200)
    next_of_kin_contact_no = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Department(TimeStampedModel):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(User, null=True)
    staff = models.ManyToManyField(User, related_name='+')

    def __str__(self):
        return self.name


class RoomType(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Room type'
        verbose_name_plural = 'Room types'


class Room(TimeStampedModel):
    room_type = models.ForeignKey(RoomType)
    room_number = models.IntegerField(default=0, blank=True)
    departmnt = models.ForeignKey(Department)

    def __str__(self):
        return '{}-{}'.format(self.room_number, self.room_type.name)


class Diagnose(TimeStampedModel):
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=0, unique=True)
    description = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.code, self.name)


class HospitalStats(TimeStampedModel):
    totalAdmins = models.IntegerField()
    totalDoctors = models.IntegerField()
    totalNurses = models.IntegerField()
    totalPatients = models.IntegerField()
    successfulLogins = models.IntegerField()
    failedLogins = models.IntegerField()
    appointmentsCreated = models.IntegerField()
    medicationsPrescribed = models.IntegerField()
    testsConducted = models.IntegerField()
    messagesSent = models.IntegerField()
    notificationsReceived = models.IntegerField()
    patientsAdmitted = models.IntegerField()
    oldestUser = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Hospital Statistics'
        verbose_name_plural = 'Hospital Statistics'


class supplier(TimeStampedModel):
    pass
