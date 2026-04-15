import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"D:\py mini pro\Mini-Project_-Pl-2_Sem-4\data\cleaned_data.csv")

yearly = df.groupby("Year")["TIV"].sum()

plt.figure(figsize=(12,6))
plt.fill_between(yearly.index, yearly.values)

plt.title("Area Chart of Total TIV over Year")
plt.xlabel("Year")
plt.ylabel("Total TIV")
plt.grid(True)
plt.tight_layout()

os.makedirs("output", exist_ok=True)

plt.savefig("output/area_tiv_year.png")
plt.show()
