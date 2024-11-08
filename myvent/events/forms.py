# events/forms.py

from django import forms
from .models import Event, RSVP

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'max_attendees']

class RSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = ['status']  # Users can choose 'attending' or 'not attending'

class EventSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Search by Title')
    location_name = forms.CharField(required=False, label='Search by Location')
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Date From')
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}), label='Date To')
    category = forms.ChoiceField(required=False, choices=[('', 'All Categories')] + Event.CATEGORY_CHOICES, label='Filter by Category')