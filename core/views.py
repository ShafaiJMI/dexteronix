from django.shortcuts import render
from .models import Service,Team

# Create your views here.
def home(request):
	services= Service.objects.all()
	context = {
	'page_title':'Dexteronix Technologies Pvt Ltd',
	'services':services,
	}
	return render(request,'home.html',context)

def about(request):
	team = Team.objects.all()
	context = {
	'page_title':'About | Dexteronix Technologies Pvt Ltd',
	'team':team,
	}
	return render(request,'about.html',context)

def project(request):
	context = {
	'page_title':'Projects | Dexteronix Technologies Pvt Ltd',
	}
	return render(request,'project.html',context)

def contact(request):
	context = {
	'page_title':'contact | Dexteronix Technologies Pvt Ltd',
	}
	return render(request,'contact.html',context)