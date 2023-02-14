import csv


filename = 'the_csv_file_format/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures from this file.
    highs = [int(row[5]) for row in reader]

print(highs)
