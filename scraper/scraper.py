import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

url = "https://en.wikipedia.org/wiki/List_of_countries_by_military_expenditure"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table", {"class": "wikitable"})

rows = table.find_all("tr")

headers = [th.text.strip() for th in rows[0].find_all("th")]

data = []
for row in rows[1:]:
    cols = [col.text.strip() for col in row.find_all(["td", "th"])]
    if len(cols) == len(headers):
        data.append(cols)

df = pd.DataFrame(data, columns=headers)

# Extract country column
df = df[[df.columns[1]]]   # usually country column
df.rename(columns={df.columns[0]: "Country"}, inplace=True)

countries = df["Country"].tolist()

# Generate dataset
final_data = []

for year in range(2000, 2024):
    for _ in range(100):
        exporter = random.choice(countries)
        importer = random.choice(countries)

        if exporter == importer:
            continue

        weapon = random.choice(["Aircraft", "Missiles", "Tanks"])
        units = random.randint(1, 50)
        tiv = units * random.randint(5, 50)

        final_data.append([exporter, importer, weapon, year, units, tiv])

final_df = pd.DataFrame(final_data, columns=[
    "Exporter", "Importer", "Weapon", "Year", "Units", "TIV"
])

final_df.to_csv("../data/raw_data.csv", index=False)

print("✅ SUCCESS!")