from django.shortcuts import render
# Create your views here.
@api_view(['POST'])
def send_geo_data(request):
    req_data = request.data
    