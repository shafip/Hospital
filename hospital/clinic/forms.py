from django import forms
from .models import *

class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    email:forms.EmailField()
    class Meta:
        model=User
        fields = ['username','email','password1','password2']