import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
num_rows = len(df)

df = df[df['Age'].notna()]


nr_copii = df[(df['Age'] < 18)].shape[0]
nr_copii_suprav = df[(df['Age'] < 18) & (df['Survived'] == 1)].shape[0]
print("copii la bord = ",nr_copii)
print("nr copii suprav = ", nr_copii_suprav)
print("procentul copiilor ce au supravietuit = ", round(nr_copii_suprav / nr_copii * 100, 2), "%")
a = nr_copii_suprav / nr_copii * 100
nr_adulti = df[(df['Age'] >= 18)].shape[0]
nr_adulti_suprav = df[(df['Age'] >= 18) & (df['Survived'] == 1)].shape[0]
b = nr_adulti_suprav / nr_adulti * 100

x = ([a , b])
mylabels = ["copii", "adulti"]
bars = plt.bar(mylabels, x)
plt.title("% of kids that surv vs % of adults that surv")
plt.ylabel('Percentages', fontsize = 12)
plt.bar_label(bars)

plt.savefig("../Images/C7.png")
plt.close()