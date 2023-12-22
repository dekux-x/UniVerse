from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]
Dormitary_Choices = [("yes","Yes"), ("no","No")]

class FilterForm(forms.Form):
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    type = forms.CharField(max_length=15)
    dormitary = forms.ChoiceField(widget=forms.RadioSelect, choices=Dormitary_Choices)

class GrantChance(forms.Form):
    program_code = forms.CharField(max_length=5)
    number_of_points = forms.IntegerField()

class Compare(forms.Form):
    first_id = forms.IntegerField()
    second_id = forms.IntegerField()
