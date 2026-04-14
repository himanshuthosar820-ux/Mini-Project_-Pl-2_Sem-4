import os
import pandas as pd
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../../data/cleaned_data.csv")
output_dir = os.path.join(base_dir, "output")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

yearly_tiv = df.groupby('Year')['TIV'].sum()

plt.figure()
yearly_tiv.plot()
plt.title("Total TIV per Year")
plt.xlabel("Year")
plt.ylabel("TIV")

plt.savefig(os.path.join(output_dir, "tiv-per-year.png"))
plt.close()