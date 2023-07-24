import requests
import pandas as pd
from bs4 import BeautifulSoup

def NBAInjuries():
    url = 'https://www.cbssports.com/nba/injuries/daily/'

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the tables with the data
    tables = soup.find_all('table', {'class': 'TableBase-table'})

    # Initialize an empty list to store all the data
    all_data = []

    # Loop through the tables and get the data
    for table in tables:
        # Get the table headers
        headers = [header.text for header in table.find_all('th')]

        # Get the table rows
        rows = table.find_all('tr')

        # Loop through the rows and get the data
        for row in rows:
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            data = {headers[i]: cols[i] for i in range(len(cols))}
            all_data.append(data)

    # Remove any empty dictionaries
    all_data = [row for row in all_data if row]

    # Clean up the keys in the dictionary
    cleaned_data = [{key.strip(): value for key, value in row.items()} for row in all_data]

    # Convert the list of dictionaries to a pandas DataFrame
    df = pd.DataFrame(cleaned_data)

    return df

# Call the function and assign the DataFrame to a variable
nba_injuries_df = NBAInjuries()

# Print the DataFrame
# print(nba_injuries_df)
