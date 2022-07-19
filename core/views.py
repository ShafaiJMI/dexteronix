from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Service,Team,Message

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
	if request.method == "POST":
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		message = request.POST.get('message')
		new_message = Message.objects.create(name=name,email=email,message=message)
		if phone:
			new_message.phone = phone
		new_message.save()
		messages.success(request, 'Thanks for writing to us!')
		return redirect('contact')

	context = {'page_title':'contact | Dexteronix Technologies Pvt Ltd',}
	return render(request,'contact.html',context)