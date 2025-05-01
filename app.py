from flask import Flask, render_template, request
import subprocess
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=None)

@app.route('/run-script', methods=['POST'])
def run_script():
    # Run the scraping script
    subprocess.run(['python', 'scrape_literacy_in_india.py'])

    # Read CSV content
    data = []
    with open('literacy_in_india.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            data.append(row)

    return render_template('index.html', data=data, headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
