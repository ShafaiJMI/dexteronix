from django.contrib import admin
from .models import Service,Team
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title']

class TeamAdmin(admin.ModelAdmin):
	list_display = ['name','role']

admin.site.register(Service,ServiceAdmin)
admin.site.register(Team,TeamAdmin)