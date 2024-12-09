from django import forms
from .models import Dancer, Group, Festival

class DancerForm(forms.ModelForm):
    class Meta:
        model = Dancer
        fields = ['name', 'age', 'style', 'group']

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'city']  

class FestivalForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ['name', 'date', 'group']  