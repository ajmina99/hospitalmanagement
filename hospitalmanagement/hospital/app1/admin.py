from django.contrib import admin

from app1.models import Doctor,Patient,Appointment

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
