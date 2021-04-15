from django.shortcuts import get_object_or_404, render
from .models import Page

# Create your views here.
def page(request, page_id):
    page =  get_object_or_404(Page, id=page_id)
    return render(request, 'pages/sample.html', {'page': page})
