import csv


filename = 'the_csv_file_format/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Show Header Row and index that belong to
    for index, column_header in enumerate(header_row):
        print(index, column_header)
