from django import forms

from main.models import Countries


class CountriesForm(forms.ModelForm):
    class Meta:
        model = Countries
        fields = "__all__"
        widgets = {"checkpoints": forms.CheckboxSelectMultiple}
