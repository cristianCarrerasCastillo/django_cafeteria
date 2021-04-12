from django.shortcuts import render
from .forms import ContactForms

# Create your views here.
def contact(request):
    contact_form = ContactForms()
    return render(request, "contact/contact.html",{'form': contact_form})