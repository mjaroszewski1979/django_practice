from django import forms
from django.forms.models import inlineformset_factory
from .models import City, Country

class CityModelForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'population']

CityFormSet = inlineformset_factory(
    Country,
    City,
    CityModelForm,
    can_delete=False,
    min_num=2,
    extra=0
)