import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, "../../data/cleaned_data.csv")
output_dir = os.path.join(base_dir, "output")

os.makedirs(output_dir, exist_ok=True)

df = pd.read_csv(data_path)

corr = df[['Units', 'TIV', 'TIV_per_unit', 'Year']].corr()

plt.figure()
sns.heatmap(corr, annot=True)
plt.title("Correlation Heatmap")

plt.savefig(os.path.join(output_dir, "correlation-heatmap.png"))
plt.close()