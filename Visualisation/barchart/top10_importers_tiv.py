import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"D:\py mini pro\Mini-Project_-Pl-2_Sem-4\data\cleaned_data.csv")

top10 = df.groupby("Importer")["TIV"].sum().nlargest(10)

plt.figure(figsize=(12,6))
top10.plot(kind="bar")

plt.title("Top 10 Importers by TIV")
plt.xlabel("Importer")
plt.ylabel("Total TIV")
plt.xticks(rotation=45)
plt.tight_layout()

os.makedirs("output", exist_ok=True)

plt.savefig("output/top10_importers_tiv.png")
plt.show()