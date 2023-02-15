import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data.
filename = 'mapping_global_data_sets/data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Get All Earthquake data
all_eq_dicts = all_eq_data['features']

mags, lons, lats, hover_texts = [], [], [], []
# Get All Earthquake magnitudes, and
# Location Data: longitude and latitude, and title
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='mapping_global_data_sets/global_earthquakes.html')
