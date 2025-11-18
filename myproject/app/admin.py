from django.contrib import admin
from app.models import *

# Register your models here.
class Admintodo(admin.ModelAdmin):
    name=Todo



admin.site.register(Todo,Admintodo)