from django import forms

class  VerificacionForm(forms.Form):
    primer_nombre = forms.CharField(max_length=255)
    apellido = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    telefono = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    codigopostal = forms.CharField(max_length=255)
    lugar = forms.CharField(max_length=255)
    stripe_token = forms.CharField(max_length=255)