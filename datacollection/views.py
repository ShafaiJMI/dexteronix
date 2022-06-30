#from django.shortcuts import render
from .serializers import DustbinSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Dustbin

# Create your views here.
def BustbinAPI(request):
	if request.method == "GET":
		try:
			queryset = Dustbin.objects.all()
			serializer = DustbinSerializer(queryset,many=True)
			return JsonResponse(serializer.data,safe=False)
		except:
			return HttpResponse(status=404)
@csrf_exempt

def UpdateLevel(request,dbnid):
	if request.method == "PUT":
		try:
			queryset = Dustbin.objects.get(dustbinid=dbnid)
			serializer = DustbinSerializer(queryset,data=request.data)
			if serializer.is_valid():
				serializer.save()
				return HttpResponse(status=200)
			else:
				return HttpResponse(status=404)
		except:
			return HttpResponse(status=400)