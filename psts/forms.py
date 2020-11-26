from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    pst_name = forms.CharField(initial="all")
    pst_type = forms.ModelChoiceField(
        required=False, empty_label="모든정보", queryset=models.PstType.objects.all()
    )
