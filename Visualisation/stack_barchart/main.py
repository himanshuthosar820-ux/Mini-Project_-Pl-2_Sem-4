import os
import pandas as pd
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../../data/cleaned_data.csv")
output_dir = os.path.join(base_dir, "output")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

pivot = df.pivot_table(index='Exporter', columns='Weapon', values='Units', aggfunc='sum', fill_value=0)

pivot.plot(kind='bar', stacked=True)
plt.title("Weapon Categories by Exporter")
plt.xticks(rotation=45)

plt.savefig(os.path.join(output_dir, "stacked-weapon-exporter.png"))
plt.close()