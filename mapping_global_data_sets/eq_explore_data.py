import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data.
filename = 'mapping_global_data_sets/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Get All Earthquake data
all_eq_dicts = all_eq_data['features']

mags, lons, lats = [], [], []
# Get All Earthquake magnitudes, and
# Location Data: longitude and latitude
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags]
    }
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='mapping_global_data_sets/global_earthquakes.html')
