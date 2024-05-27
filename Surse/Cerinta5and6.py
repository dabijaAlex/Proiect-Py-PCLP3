import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
num_rows = len(df)


df_0_20 = df[df['Age'] <= 20]

df_21_40 = df[df['Age'] <= 40]
df_21_40 = df_21_40[df_21_40['Age'] >= 21]

df_41_60 = df[df['Age'] <= 60]
df_41_60 = df_41_60[df_41_60['Age'] >= 41]

df_61plus = df[df['Age'] >= 61]

print(len(df_0_20), "persoane in categoria 0 - 20")
print(len(df_21_40), "persoane in categoria 21 - 40")
print(len(df_41_60), "persoane in categoria 41 - 60")
print(len(df_61plus), "persoane in categoria 61 +")

nan_count = df.isna().sum()
print(nan_count['Age'], "persoane nu le stim varsta")


df.insert(1, "AgeGroup", "")
for i in range(0,num_rows):
    if df['Age'][i] <= 20:
        df.loc[i, "AgeGroup"] = 1

    if df['Age'][i] <= 40 and df['Age'][i] >= 21:
        df.loc[i, "AgeGroup"] = 2

    if df['Age'][i] <= 60 and df['Age'][i] >= 41:
        df.loc[i, "AgeGroup"] = 3

    if df['Age'][i] >= 61:
        df.loc[i, "AgeGroup"] = 4

# print(df.head(100))

a = df['AgeGroup'].value_counts()[1] / (num_rows - nan_count["Age"]) * 100
b = df['AgeGroup'].value_counts()[2] / (num_rows - nan_count["Age"]) * 100
c = df['AgeGroup'].value_counts()[3] / (num_rows - nan_count["Age"]) * 100
d = df['AgeGroup'].value_counts()[4] / (num_rows - nan_count["Age"]) * 100

# unknown = 100 - a - b - c - d
x = np.array([a, b, c, d])
# print(x)
mylabels = ["[0-20]", "[21-40]", "[41-60]", "61+"]
plt.pie(x, autopct='%1.1f%%', labels = mylabels)
plt.title('Distribution between ages')

plt.savefig("../Images/C52.png")
plt.close()

df = df[df['Age'].notna()]
total_barbati_suprav = (df.loc[(df['Sex'] == "male") & (df['Survived'] == 1)]).shape[0]
male_0_20_alive = (df_0_20.loc[(df_0_20['Sex'] == "male") & (df_0_20['Survived'] == 1)]).shape[0]
male_21_40_alive = (df_21_40.loc[(df_21_40['Sex'] == "male") & (df_21_40['Survived'] == 1)]).shape[0]
male_41_60_alive = (df_41_60.loc[(df_41_60['Sex'] == "male") & (df_41_60['Survived'] == 1)]).shape[0]
male_60_plus_alive = (df_61plus.loc[(df_61plus['Sex'] == "male") & (df_61plus['Survived'] == 1)]).shape[0]

print("au supravietuit", total_barbati_suprav, "barbati")
print("din categ 0 - 20 au supravietuit", male_0_20_alive, "barbati")
print("din categ 21 - 40 au supravietuit", male_21_40_alive, "barbati")
print("din categ 41 - 60 au supravietuit", male_41_60_alive, "barbati")
print("din categ 61 + au supravietuit", male_60_plus_alive, "barbati")

print('\n')


a = (df_0_20.loc[(df_0_20['Sex'] == "male") & (df_0_20['Survived'] == 1)]).shape[0] / (df_0_20.loc[(df_0_20['Sex'] == "male")].shape[0]) * 100
b = (df_21_40.loc[(df_21_40['Sex'] == "male") & (df_21_40['Survived'] == 1)]).shape[0] / (df_21_40.loc[(df_21_40['Sex'] == "male")].shape[0]) * 100
c = (df_41_60.loc[(df_41_60['Sex'] == "male") & (df_41_60['Survived'] == 1)]).shape[0] / (df_41_60.loc[(df_41_60['Sex'] == "male")].shape[0]) * 100
d = (df_61plus.loc[(df_61plus['Sex'] == "male") & (df_61plus['Survived'] == 1)]).shape[0] / (df_61plus.loc[(df_61plus['Sex'] == "male")].shape[0]) * 100

x = [a, b, c, d]
mylabels = ["[0-20]", "[21-40]", "[41-60]", "61+"]
bars = plt.bar(mylabels, x)
plt.title("Percentage of men that survived based on age group")
plt.xlabel('Age Groups', fontsize=12)
plt.ylabel('Percentages', fontsize=12)
plt.bar_label(bars)

plt.savefig("../Images/C6.png")
plt.close()
