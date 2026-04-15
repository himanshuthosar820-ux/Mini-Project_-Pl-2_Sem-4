import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"D:\py mini pro\Mini-Project_-Pl-2_Sem-4\data\cleaned_data.csv")
weapons = df["Weapon"].unique()
data = [df[df["Weapon"] == weapon]["TIV_per_unit"] for weapon in weapons]

plt.figure(figsize=(12,6))
plt.violinplot(data, showmeans=True)
plt.xticks(range(1, len(weapons)+1), weapons, rotation=45)
plt.title("Violin Plot of TIV_per_unit by Weapon")
plt.xlabel("Weapon")
plt.ylabel("TIV_per_unit")
plt.tight_layout()
plt.savefig("output/violin_tiv_weapon.png")

plt.show()