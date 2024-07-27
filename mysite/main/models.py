from django.db import models
from googleplaces import GooglePlaces
import os


class Place(models.Model):
    place_name = models.CharField(max_length=200)
    lat = models.DecimalField()
    long = models.DecimalField()
    
    def getNearbyResources(resource_name):
        google_places = GooglePlaces(os.getenv('GOOGLE_PLACES_KEY'))
        query_result = google_places.text_search(
                            lat_lng={'lat': 40.740614, 'lng': -73.976601}, 
                            query='Homeless Shelter',
                            radius=5000)

        for place in query_result.places:
            place.get_details()
            name = place.name
            latitude = place.geo_location['lat']
            longitude = place.geo_location['lng']
            return (f"Name: {name}, Latitude: {latitude}, Longitude: {longitude}")
            
    
# Create your models here.
