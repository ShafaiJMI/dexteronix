from django.contrib import admin
from .models import Dustbin
# Register your models here.

class DustbinAdmin(admin.ModelAdmin):
	list_display = ['dustbinid','location','level','updated_at']

admin.site.register(Dustbin,DustbinAdmin)