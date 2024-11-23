from django import forms

class CountrySearchForm(forms.Form):
    q = forms.CharField(
        label="Search for a country",
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter country name', 'class': 'form-control'})
    )

