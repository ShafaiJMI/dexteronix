from django.contrib import admin
from .models import Service,Team,Message
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['title']

class TeamAdmin(admin.ModelAdmin):
	list_display = ['name','role']

class MessageAdmin(admin.ModelAdmin):
	list_display = ['name','sent_at']

admin.site.register(Service,ServiceAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Message,MessageAdmin)