from shapely.geometry import Polygon, MultiPolygon
from geopy.distance import geodesic
import json
from disaster_data import get_disaster_data
from decouple import config


#idea for the function is that it computes the total area of all pol

# Assuming get_disaster_data fetches JSON data and returns it as a dictionary
json_data = get_disaster_data("FLOOD", config("KEY"), "h1")

def calculate_circle_radius_from_geojson(geojson_data):
    polygons = []
    for feature in geojson_data['features']:
        geom = feature['geometry']
        if geom['type'] == 'Polygon':
            polygons.append(Polygon(geom['coordinates'][0]))
        elif geom['type'] == 'MultiPolygon':
            for coords in geom['coordinates']:
                polygons.append(Polygon(coords[0]))

    if not polygons:
        return None, None  # No polygons found

    # Combine all polygons into a single MultiPolygon for centroid calculation
    combined_polygon = MultiPolygon(polygons)
    centroid = combined_polygon.centroid

    # Calculate the radius as the maximum distance from the centroid to the polygon's exterior points
    max_distance = 0
    for poly in combined_polygon.geoms:
        for coord in poly.exterior.coords:
            distance = geodesic((centroid.y, centroid.x), (coord[1], coord[0])).meters
            max_distance = max(max_distance, distance)

    return max_distance, (centroid.y, centroid.x)

# Example usage with the JSON data
radius, center = calculate_circle_radius_from_geojson(json_data)
if radius is not None:
    print(f"Radius: {radius + 2000} meters") #we add an extra 2 kilometers for safety or we could not
    print(f"Center: {center}")
else:
    print("No polygons found in the GeoJSON data.")