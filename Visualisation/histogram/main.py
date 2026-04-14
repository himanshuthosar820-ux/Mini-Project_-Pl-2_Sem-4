import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

base_dir = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(base_dir, "../../data/cleaned_data.csv")
output_dir = os.path.join(base_dir, "outputs")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

plt.figure()
plt.hist(df['TIV'], bins=20, edgecolor='black')
plt.title("Distribution of TIV")
plt.xlabel("TIV")
plt.ylabel("Frequency")
plt.savefig(os.path.join(output_dir, "histogram-tiv.png"))
plt.close()

plt.figure()
sns.kdeplot(data=df, x="Units")
plt.title("Distribution of Units")
plt.xlabel("Units")
plt.ylabel("Density")
plt.savefig(os.path.join(output_dir, "histogram-units.png"))
plt.close()

plt.figure()
plt.hist(df['TIV_per_unit'], bins=20, edgecolor='black')
plt.title("Distribution of TIV per Unit")
plt.xlabel("TIV per Unit")
plt.ylabel("Frequency")
plt.savefig(os.path.join(output_dir, "histogram-tiv-per-unit.png"))
plt.close()