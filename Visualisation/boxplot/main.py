import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

base_dir = os.path.dirname(os.path.abspath(__file__))

data_path = os.path.join(base_dir, "../../data/cleaned_data.csv")
output_dir = os.path.join(base_dir, "output")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

plt.figure()
sns.boxplot(x=df['TIV_per_unit'])
plt.title("Boxplot of TIV per Unit")
plt.xlabel("TIV per Unit")

plt.savefig(os.path.join(output_dir, "boxplot-tiv-per-unit.png"))
plt.close()