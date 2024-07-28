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
    addy = data['address']
    coords = dd.addy_to_coords(addy)
    lon = coords[0]
    lat = coords[1]
    ret = {}
    ret['type'] = dd.get_active_hazard(lon, lat)
    ret['news'] = []
    ret['refuge'] = dd.find_refuge(lat, lon)
    for x in ret['type']:
        ret['news'].append(dd.get_news(x, addy))
    return Response(ret, status=status.HTTP_200_OK)





def index(request):
    context = {"message": "Hello"}  # Use a dictionary here
    return render(request, "main/index.html", context)

def main_page(request):
    return render(request, "main/mainpage.html")