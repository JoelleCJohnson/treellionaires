import requests
import pandas as pd

overpass_url = "http://overpass-api.de/api/interpreter"

# Overpass QL query
overpass_query = """
[out:json];
(
  node["highway"="bus_stop"](26.2703,-80.3876,26.9516,-80.0314);
);
out body;
"""

overpass_query2 = """
[out:json];
(
  node["highway"="bus_stop"](25.3935,-80.2112,26.2159,-80.0742);
);
out body;
"""

overpass_query3 = """
[out:json];
(
  node["highway"="bus_stop"](25.2524,-80.4320,25.8840,-80.1416);
);
out body;
"""

# Make the request
palm_beach_bus_stops = requests.get(overpass_url, params={'data': overpass_query})
broward_bus_stops = requests.get(overpass_url, params={'data': overpass_query2})
miami_bus_stops = requests.get(overpass_url, params={'data': overpass_query3})


# Parse the palm_beach_bus_stops
stops = []

for element in palm_beach_bus_stops.json()['elements']:
    if 'lat' in element and 'lon' in element:
        stops.append({"lat": element['lat'], "lon": element['lon']})

for element in broward_bus_stops.json()['elements']:
    if 'lat' in element and 'lon' in element:
        stops.append({"lat": element['lat'], "lon": element['lon']})

for element in miami_bus_stops.json()['elements']:
    if 'lat' in element and 'lon' in element:
        stops.append({"lat": element['lat'], "lon": element['lon']})

stops_df = pd.DataFrame(stops)
stops_df.to_csv('bus_stops.csv', index=False)
