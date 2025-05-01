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
    data = []
    headers = []
    try:
        # Run the external script
        subprocess.run(['python', 'scrape_literacy_in_india.py'], check=True)

        # Ensure the CSV exists before reading
        csv_path = 'literacy_in_india.csv'
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"{csv_path} not found.")

        # Read CSV content
        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            for row in reader:
                data.append(row)
    except Exception as e:
        return render_template('index.html', data=None, headers=None, error=str(e))

    return render_template('index.html', data=data, headers=headers)

if __name__ == '__main__':
    app.run(debug=True)
