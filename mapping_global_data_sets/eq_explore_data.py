import json


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

# Print first 10 Magnitude
print(mags[:10])
# Print first 5 longitude
print(lons[:5])
# Print first 5 latitude
print(lats[:5])
