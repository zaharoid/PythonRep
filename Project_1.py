import csv
import pygal
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded'

        file = request.files['file']

        if file.filename == '':
            return 'No file selected'

        if not file.filename.endswith('.csv'):
            return 'Invalid file format. Please upload a CSV file.'

        file_path = 'tmp.csv'
        file.save(file_path)

        x, y, z = read_data_from_csv(file_path)
    else:
        # Default synthetic data
        x = [1, 2, 3, 4, 5]
        y = [2, 4, 6, 8, 10]

    chart_svg = create_chart(x, y)

    return render_template('index.html', chart_svg=chart_svg, now=datetime.now(),)
with open("factbook.csv", 'r') as file:
     reader = csv.reader(file, delimiter=';')
     next(reader)
     next(reader)
     areas = []
     countries = []
     GPD = []
     for row in reader:
         areas.append(row[1])
         countries.append(row[0])
         GPD.append(float(row[11].strip() if row[11].strip() != '' else 0))

filtredIndexes = list(filter(lambda i: int(areas[i]) > 1000, range(len(areas))))

filtredItems = [countries[i] for i in filtredIndexes]

print(areas)
print(countries)
print(GPD)
print(filtredIndexes)
print(filtredItems)


def create_chart(countries, GPD):
    line_chart = pygal.Line()
    line_chart.title = 'GDP of countries with an area of less than 1,000'
    line_chart.countries_labels = countries
    line_chart.add("GDP's", GPD)

    return line_chart.render().decode().strip()



