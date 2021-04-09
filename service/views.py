from django.shortcuts import render
from .models import Service

# Create your views here.
def service(request):
    services = Service.objects.all()
    return render(request, "service/services.html", {'var_services':services})
