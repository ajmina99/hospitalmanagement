from django import forms
from .models import Doctor, Appointment


class doctorform(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class appointmentform(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'
        widgets={
            'appointment_date':forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'symptoms':forms.Textarea(attrs={'rows':4}),
        }
