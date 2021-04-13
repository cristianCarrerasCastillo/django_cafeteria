from django.contrib import admin
from django.db import models
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'edited')
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists():
            return ('key', 'name')
        else:
            return ('created', 'edited')

admin.site.register(Link, LinkAdmin)