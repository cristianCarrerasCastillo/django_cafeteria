from django import forms

class ContactForms(forms.Form):
    name = forms.CharField(label='Nombre',required=True, widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'Tu Nombre'}
    ), min_length=4, max_length=50)
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={'class':'form-control','placeholder':"Tu@email.com"}
    ),min_length=4, max_length=100)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'class':'form-control','rows':3, 'placeholder':'Escribe tu mensaje'}
    ),min_length=10, max_length=1000)