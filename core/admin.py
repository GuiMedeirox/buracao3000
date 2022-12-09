from django.contrib import admin
from django.apps import apps
from .models import buracos, buracos_status


# Register your models here.

admin.site.register(buracos, buracos_status)
