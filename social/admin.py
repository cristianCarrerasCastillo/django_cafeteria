from django.contrib import admin
from django.db import models
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'edited')

admin.site.register(Link, LinkAdmin)