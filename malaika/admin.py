# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# app import
from malaika.models import Room
from reception.models import Patient, Diagnose, In_patient, Out_patient
from staff.models import Doctor
from operations.models import Treatment
from finance.models import Billing

# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Diagnose)
admin.site.register(Room)
admin.site.register(In_patient)
admin.site.register(Out_patient)
admin.site.register(Treatment)
admin.site.register(Billing)
