from django.contrib import admin
from app.models import *

# Register your models here.
class Admintodo(admin.ModelAdmin):
    name=Todo



admin.site.register(Todo,Admintodo)
class Admincompleted(admin.ModelAdmin):
    name=Completemodel



admin.site.register(Completemodel,Admincompleted)
class Admintrash(admin.ModelAdmin):
    name=Trashmodel



admin.site.register(Trashmodel,Admintrash)