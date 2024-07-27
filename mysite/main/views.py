from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
@api_view(['POST'])
def send_geo_data(request):
    req_data = request.data
    
    
def index(request):
    context = {"message": "Hello"}  # Use a dictionary here
    return render(request, "main/hi.html", context)
    