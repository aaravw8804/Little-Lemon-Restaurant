from .models import Bookings;
from django import forms;

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = '__all__'