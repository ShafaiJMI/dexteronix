from django.urls import path
from . import views

urlpatterns =[
    path('api/',views.BustbinAPI,name="dustbinapi"),
    path('levelapi/<dbnid>/',views.UpdateLevel,name="updatelevel"),
]