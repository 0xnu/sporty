import requests
from bs4 import BeautifulSoup

def BundesligaTable():

  url = "https://www.livescores.com/football/germany/bundesliga/?tz=1"

  page = requests.get(url)
  soup = BeautifulSoup(page.content, "lxml")

  table = soup.find("table", {"class": "Yd Zd"})

  # Extract the table rows
  rows = table.find_all("tr")

  for row in rows:
    cols = row.find_all("td")
    row_data = []
    for col in cols:
      row_data.append(col.text)
    if row_data:  # Check if row_data is not empty
      yield row_data  # Yield row_data for each row

# Use the BundesligaTable function
bundesligatable = list(BundesligaTable())  # Convert the generator to a list
#print(bundesligatable)
