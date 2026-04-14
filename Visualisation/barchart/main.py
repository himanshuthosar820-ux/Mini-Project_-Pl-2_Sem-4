import os
import pandas as pd
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../../data/cleaned_data.csv")
output_dir = os.path.join(base_dir, "output")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

avg_tiv = df.groupby('Weapon')['TIV_per_unit'].mean().sort_values()

plt.figure()
avg_tiv.plot(kind='bar')
plt.title("Average TIV per Unit by Weapon")
plt.xticks(rotation=45)

plt.savefig(os.path.join(output_dir, "avg-tiv-per-weapon.png"))
plt.close()