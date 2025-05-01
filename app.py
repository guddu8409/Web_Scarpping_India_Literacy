from flask import Flask, render_template, request
import subprocess
import csv
import os

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
    # Bind the app to 0.0.0.0 to allow external access, and use the dynamic port
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
