import geopandas as gpd
from shapely.geometry import shape, MultiPolygon, Polygon
from geopy.distance import geodesic

def create_circle_and_calculate_distance(geojson, buffer_distance):
    # Load GeoJSON data
    gdf = gpd.GeoDataFrame.from_features([geojson])

    # Extract the geometry
    geom = gdf.geometry.iloc[0]
    
    # Check if the geometry is a Polygon or MultiPolygon
    if isinstance(geom, Polygon):
        centroid = geom.centroid
        buffer = geom.buffer(buffer_distance)
    elif isinstance(geom, MultiPolygon):
        # For MultiPolygon, get the centroid of the bounding box of the union
        bounding_box = geom.minimum_rotated_rectangle
        centroid = bounding_box.centroid
        buffer = geom.buffer(buffer_distance)
    else:
        raise TypeError("GeoJSON must be a Polygon or MultiPolygon")

    # Calculate distance from the centroid to the boundary of the buffer
    distance = centroid.distance(buffer.boundary)
    
    # Convert distance to meters (approximate conversion)
    distance_meters = distance * 1000
    
    # Create a circle around the centroid
    circle = centroid.buffer(buffer_distance)

    return circle, distance_meters

# Example MultiPolygon GeoJSON
geojson_multipolygon = {
    "type": "Feature",
    "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
            [
                [
                    [-100.0, 40.0],
                    [-101.0, 40.0],
                    [-101.0, 41.0],
                    [-100.0, 41.0],
                    [-100.0, 40.0]
                ]
            ],
            [
                [
                    [-99.5, 40.5],
                    [-99.0, 40.5],
                    [-99.0, 41.0],
                    [-99.5, 41.0],
                    [-99.5, 40.5]
                ]
            ]
        ]
    },
    "properties": {}
}

buffer_distance = 0.05  # in degrees (approximately 5 km)

circle, distance_meters = create_circle_and_calculate_distance(geojson_multipolygon, buffer_distance)

print(f"Circle Geometry: {circle}")
print(f"Distance from centroid to circle boundary: {distance_meters:.2f} meters")

# Example usage
geojson = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-100.0, 40.0],
                [-101.0, 40.0],
                [-101.0, 41.0],
                [-100.0, 41.0],
                [-100.0, 40.0]
            ]
        ]
    },
    "properties": {}
}

buffer_distance = 0.05  # in degrees (approximately 5 km)

circle, distance_meters = create_circle_and_calculate_distance(geojson, buffer_distance)

print(f"Circle Geometry: {circle}")
print(f"Distance from centroid to circle boundary: {distance_meters:.2f} meters")