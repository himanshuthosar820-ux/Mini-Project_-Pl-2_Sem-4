import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"D:\py mini pro\Mini-Project_-Pl-2_Sem-4\data\cleaned_data.csv")

top_exporters = df.groupby("Exporter")["TIV"].sum().nlargest(5).index

plt.figure(figsize=(12,6))

for exporter in top_exporters:
    yearly = df[df["Exporter"] == exporter].groupby("Year")["TIV"].sum()
    plt.plot(yearly.index, yearly.values, marker="o", label=exporter)

plt.title("TIV over Year for Top Exporters")
plt.xlabel("Year")
plt.ylabel("TIV")
plt.legend()
plt.grid(True)
plt.tight_layout()

os.makedirs("output", exist_ok=True)

plt.savefig("output/tiv_top_exporters.png")
plt.show()
