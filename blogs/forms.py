from django import forms
from . import models


class SearchForm(forms.Form):

    post_type = forms.ModelChoiceField(
        required=False, empty_label="Any Kind", queryset=models.PostType.objects.all()
    )
