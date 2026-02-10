#The python package shall first be installed using the command: pip install Topsis-Gurmandeep-102303764
#Then run the package from the command line: python -m topsis_gurmandeep_102303764.topsis sample_data.csv "4,2,1,1" "+,-,-,-" output.csv
#The complete package can be accessed at: https://pypi.org/project/Topsis-Gurmandeep-102303764/

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("output.csv")

plt.bar(df["Model"], df["Topsis Score"])
plt.xticks(rotation=20)
plt.title("TOPSIS Scores for Conversational Models")

plt.show()
