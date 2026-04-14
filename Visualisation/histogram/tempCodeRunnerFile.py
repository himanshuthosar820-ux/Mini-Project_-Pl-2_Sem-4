import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv("../../data/cleaned_data.csv")

plt.hist(df['TIV'], bins=20, edgecolor='black')
plt.title("Distribution of TIV")
plt.xlabel("TIV (Trend Indicator Value)")
plt.ylabel("Frequency")

plt.savefig("../../Visualisation/histogram/outputs/histogram-tiv.png")

sns.kdeplot(data=df, x="Units")
plt.title("Distribution of Units")
plt.xlabel("Units")
plt.ylabel("Frequency")
plt.savefig("../../Visualisation/histogram/outputs/histogram-units.png")
plt.show()