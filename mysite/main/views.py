from django.shortcuts import render
from rest_framework.decorators import api_view
from django.urls import path
from django.http import HttpResponse
from django.template import loader
import disaster_data as dd
from decouple import config
# Create your views here.
@api_view(['POST'])
def get_active(request):
    data = request.data
    lat = data['lat']
    lon = data['lon']
    return dd.get_active_hazard(lat, lon)


    

def index(request):
    context = {"message": "Hello"}  # Use a dictionary here
    return render(request, "main/index.html", context)

def main_page(request):
    return render(request, "main/mainpage.html")