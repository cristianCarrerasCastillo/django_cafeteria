from django.contrib import admin
from django.db import models
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'edited')

admin.site.register(Page, PageAdmin)