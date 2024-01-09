from django import forms
from django.forms import ModelForm
from .models import Event, Registration


class Eventfrom(forms.Form):
    title = forms.CharField(label='Event title', widget=forms.TextInput, max_length=64, required=True)
    description = forms.CharField(label='Discription for event', widget=forms.Textarea, max_length=256)
    date = forms.DateTimeField(label='date and time', widget=forms.DateTimeInput)
    location = forms.CharField(label='location', max_length=64)


class Event_model(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        # fields = ['title', 'description', 'date', 'location']


class RegistrationForm(forms.Form):
    name = forms.CharField(label='Enter your name', max_length=64, widget=forms.TextInput, )
    email = forms.EmailField(label='Enter your email', widget=forms.EmailInput, )


class Registration_modle(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
