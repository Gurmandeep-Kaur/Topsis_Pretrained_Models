import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output.csv")

plt.bar(df["Model"], df["Topsis Score"])
plt.xticks(rotation=20)
plt.title("TOPSIS Scores for Conversational Models")
plt.show()