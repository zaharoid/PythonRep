import csv
def read_data_from_csv(file_path):
    areas = []
    countries = []
    GDP = []

    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        next(reader)

        for row in reader:
            areas.append(row[1])
            countries.append(row[0])
            GDP.append(int(row[9].strip() if row[9].strip() != '' else 0))

    return areas, countries, GDP