from django import forms

class AnadirAlCarritoForm(forms.Form):
    quantity = forms.IntegerField()