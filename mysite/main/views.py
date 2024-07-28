from django.shortcuts import render
from rest_framework.decorators import api_view
from . import disaster_data as dd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def get_active(request):
    data = request.data
    lat = data['lat']
    lon = data['lon']
    ret = {}
    ret['data'] = dd.get_active_hazard(lat, lon)
    
    ret['refuge'] = dd.find_refuge(lat, lon)
    ret['news'] = dd.get_news() 
    return Response(ret, status=status.HTTP_200_OK)





def index(request):
    context = {"message": "Hello"}  # Use a dictionary here
    return render(request, "main/index.html", context)

def main_page(request):
    return render(request, "main/mainpage.html")