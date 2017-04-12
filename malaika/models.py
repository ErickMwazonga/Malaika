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


class Patient(PersonDetails):
    contact_no = models.CharField(max_length=200)
    next_of_kin = models.CharField(max_length=200)

    def __str__(self):
        return '{}-{}'.format(self.first_name,self.last_name)


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


class Diagnose(models.Model):
    name = models.CharField(max_length=200)
    code = models.IntegerField(default=0, unique=True)
    description = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.code, self.name)


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


class Treatment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=None)
    date = models.DateField(default=timezone.now().date())
    symptoms = models.TextField
    diagnosis = models.ForeignKey(Diagnose, on_delete=None)
    doctors_comments = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.patient, self.doctor, self.diagnosis)


class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    charges = models.CharField(max_length=200, default=0)

    def __str__(self):
        return '{}-{}'.format(self.patient, self.charges)
