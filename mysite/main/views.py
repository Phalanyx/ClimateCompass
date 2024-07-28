from django.shortcuts import render
from rest_framework.decorators import api_view
from . import disaster_data as dd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import groq_ai2 as gq2
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
    if (ret['type'] == None):
        return Response("", status=status.HTTP_200_OK)
    ret['news'] = []
    ret['refuge'] = dd.find_refuge(lat, lon, addy)
    for x in ret['type']['episode_type']:
        ret['news'].append(dd.get_news(x, addy))
    return Response(ret, status=status.HTTP_200_OK)

@api_view(['POST'])
def get_relocation(request):
    data = request.data
    addy = data['address']
    ret = []
    ret.append(gq2.get_location_info_goverment_aid_polices(addy))
    ret.append(gq2.get_location_info_useful_knowledge(addy))
    ret.append(gq2.get_location_info_emergency_contacts(addy))
    print(ret)
    return Response(ret, status=status.HTTP_200_OK)



def index(request):
    context = {"message": "Hello"}  # Use a dictionary here
    return render(request, "main/index.html", context)

def main_page(request):
    return render(request, "main/mainpage.html")