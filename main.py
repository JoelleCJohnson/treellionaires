import os
import json
import requests
import pandas as pd

# palm beach county tree data
palm_beach_county_tree_data = requests.get('https://overpass-api.de/api/interpreter?data=[out:json];area[name="Palm Beach County"]->.a;(node["natural"="tree"](area.a););out body;')
broward_county_tree_data = requests.get('https://overpass-api.de/api/interpreter?data=[out:json];area[name="Broward County"]->.a;(node["natural"="tree"](area.a););out body;')
miami_dade_county_tree_data = requests.get('https://overpass-api.de/api/interpreter?data=[out:json];area[name="Miami-Dade County"]->.a;(node["natural"="tree"](area.a););out body;')

trees = []
for tree in palm_beach_county_tree_data.json()['elements']:
    # get zip from US ZIP Codes to Longitude and Latitude dataset
    tree = {"lat": tree['lat'], "lon": tree['lon']}
    trees.append(tree)

for tree in broward_county_tree_data.json()['elements']:
    tree = {"lat": tree['lat'], "lon": tree['lon']}
    trees.append(tree)

for tree in miami_dade_county_tree_data.json()['elements']:
    tree = {"lat": tree['lat'], "lon": tree['lon']}
    trees.append(tree)


# write to file
trees_df = pd.DataFrame(trees)
trees_df.to_csv('trees.csv', index=False)
