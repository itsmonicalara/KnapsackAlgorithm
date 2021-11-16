from django.db import models
from django import forms

#Create your forms here
class ItemsForm(forms.Form):
    name = forms.CharField()
    value = forms.IntegerField()
    weight = forms.IntegerField()
    
