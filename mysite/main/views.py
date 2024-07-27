from django.shortcuts import render
from rest_framework.decorators import api_view
from django.urls import path
from . import views
from django.http import HttpResponse
from django.template import loader


# Create your views here.
@api_view(['POST'])
def send_geo_data(request):
    req_data = request.data
    

def index(request):
    context = {"message": "Hello"}  # Use a dictionary here
    return render(request, "main/index.html", context)

def main_page(request):
    return render(request, "main/mainpage.html")