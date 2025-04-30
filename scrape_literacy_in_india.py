import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Literacy_in_India"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
else:
    print("Page successfully loaded.")

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})

if table:
    print("Table found!")
    rows = table.find_all('tr')
    
    state_literacy_data = []
    
    for i, row in enumerate(rows[1:]): 
        cols = row.find_all('td')
        
        raw_data = [col.get_text(strip=True) for col in cols]
        print(f"Raw Row {i}: {raw_data}") 

        if len(cols) >= 3:
            rank = raw_data[0]
            state_name = raw_data[1]
            literacy_rate = raw_data[2]
            
            
            state_literacy_data.append({
                'Rank': rank,
                'State': state_name,
                'Literacy Rate': literacy_rate,
            })
    
    if state_literacy_data:
        print(f"Data successfully collected. Writing to CSV file...")

        # Write the data to a CSV file ---
        csv_filename = 'literacy_in_india.csv'

        try:
            with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['Rank', 'State', 'Literacy Rate'])
                writer.writeheader()
                writer.writerows(state_literacy_data)
            print(f"Data successfully saved to {csv_filename}")
        except Exception as e:
            print(f"Failed to write to CSV. Error: {e}")
    else:
        print("No data found to write to CSV.")
else:
    print("No table found!")
