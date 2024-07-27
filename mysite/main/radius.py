from shapely.geometry import Polygon, MultiPolygon
from geopy.distance import geodesic
import json

def calculate_circle_radius_from_geojson(json_file_path):
    with open(json_file_path, 'r') as f:
        geojson_data = json.load(f)

    polygons = []
    for feature in geojson_data['features']:
        geom = feature['geometry']
        if geom['type'] == 'Polygon':
            # Directly append the Polygon object
            polygons.append(Polygon(geom['coordinates'][0]))
        elif geom['type'] == 'MultiPolygon':
            # For MultiPolygon, iterate over each polygon and append
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

json_file_path = '/Users/danielvenistan/Documents/GitHub/starterhacks/mysite/main/message.json'  # Update this path
radius, center = calculate_circle_radius_from_geojson(json_file_path)
if radius is not None:
    print(f"Radius: {radius} meters")
    print(f"Center: {center}")
else:
    print("No polygons found in the GeoJSON file.")

