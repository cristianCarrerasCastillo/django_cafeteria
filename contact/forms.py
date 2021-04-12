from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label='Nombre',required=True)
    email = forms.EmailField(label='Email', required=True)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea)