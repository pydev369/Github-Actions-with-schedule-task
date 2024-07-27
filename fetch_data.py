import os
import requests
from datetime import datetime

def fetch_and_store_data():
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    access_token = os.getenv('ACCESS_TOKEN')
    api_key = os.getenv('API_KEY')

    # Replace with the actual API endpoint
    api_url = "https://api.example.com/data"

    # Fetch data from the API
    response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})
    data = response.json()

    # Create directory structure Data/Month/Day
    today = datetime.now()
    month = today.strftime('%B')
    day = today.strftime('%d')

    directory = os.path.join('Data', month, day)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save data to a file
    file_path = os.path.join(directory, 'data.json')
    with open(file_path, 'w') as file:
        json.dump(data, file)

    print(f"Data saved to {file_path}")

if __name__ == "__main__":
    fetch_and_store_data()
