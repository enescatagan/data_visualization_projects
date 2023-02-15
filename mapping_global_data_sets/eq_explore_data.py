import json

# Explore the structure of the data.
filename = 'mapping_global_data_sets/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# Get All Earthquake data
all_eq_dicts = all_eq_data['features']


mags = []
# Get All Earthquake magnitudes
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

# Print first 10 Magnitude
print(mags[:10])
