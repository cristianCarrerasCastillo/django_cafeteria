from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForms

# Create your views here.
def contact(request):
    contact_form = ContactForms()
    if request.method == "POST":
        contact_form = ContactForms(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #Enviamos el correo y redireccionamos 
            email = EmailMessage(
                'La caffetiera: Nuevo mensaje de contacto',
                'De {} <{}>\n\nEscribió:\n\n{}'.format(name, email, content),
                "no.contestar@inbox.mailtrap.io",
                ['14227d4f92-a5d793@inbox.mailtrap.io'],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?Fail')

    return render(request, "contact/contact.html",{'form': contact_form})