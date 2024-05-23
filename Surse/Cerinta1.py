#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('train.csv')
print(df.head())
num_cols = len(df.columns)
print("nr coloane = ", num_cols)
print(df.dtypes)

print("\n")

nan_count = df.isna().sum()
print(nan_count)
print("\n")

num_rows = len(df)
print("nr linii = ", num_rows)
print("\n")

if (df.duplicated().sum()):
    print("there are some duplicates\n")
else:
    print("no duplicates\n")

fig, axs = plt.subplots(1, 3)

x = np.array([df['Survived'].value_counts()[1] / num_rows * 100, df['Survived'].value_counts()[0] / num_rows * 100])
mylabels = ["Survived", "Not Survived"]
axs[0].pie(x, autopct='%1.1f%%', labels = mylabels)

y = np.array([df['Pclass'].value_counts()[1] / num_rows * 100, df['Pclass'].value_counts()[2] / num_rows * 100, df['Pclass'].value_counts()[3] / num_rows * 100])
mylabels_class = ["First Class", "Sec Class", "Third Class"]
axs[1].pie(y, autopct='%1.1f%%', labels = mylabels_class)

z = np.array([df['Sex'].value_counts()['male'] / num_rows * 100, df['Sex'].value_counts()['female'] / num_rows * 100])
mylabels_gender = ["Male", "Female"]
axs[2].pie(z, autopct='%1.1f%%', labels = mylabels_gender)


plt.tight_layout()
plt.savefig("img1.png")
plt.close()

######################################################

ageDist = df['Age'].values.tolist()
plt.hist(ageDist)
plt.title("Age Distribution")
plt.ylabel('number of people', fontsize = 12)
plt.xlabel('Ages', fontsize = 12)

plt.savefig("./../Histograms/ageDist.png")
plt.close()

############

a = df[(df['Survived'] == 0)].shape[0]
b = df[(df['Survived'] == 1)].shape[0]
x = ([a, b])
mylabels = ["Dead", "Survived"]
bars = plt.bar(mylabels, x)
plt.title("Survival Distribution")
plt.ylabel('number of people', fontsize = 12)
plt.bar_label(bars)

plt.savefig("./../Histograms/SurvivalDist.png")
plt.close()

###############

a = df[(df['Pclass'] == 1)].shape[0]
b = df[(df['Pclass'] == 2)].shape[0]
c = df[(df['Pclass'] == 3)].shape[0]
x = ([a, b, c])
mylabels = ["1", "2", "3"]
bars = plt.bar(mylabels, x)
plt.ylabel('number of people', fontsize = 12)
plt.xlabel('Class', fontsize = 12)
plt.title("Pclass Distribution")
plt.bar_label(bars)



plt.savefig("./../Histograms/Pclass.png")
plt.close()


#############
SibSpDist = df['SibSp'].values.tolist()
plt.hist(SibSpDist, log = 1)
plt.title("SibSp Distribution")

plt.savefig("./../Histograms/SibSp.png")
plt.close()


##############
ParchDist = df['Parch'].values.tolist()
plt.hist(ParchDist, bins = 3)
plt.title("Parch Distribution")

plt.savefig("./../Histograms/Parch.png")
plt.close()

###########

FareDist = df['Fare'].values.tolist()
plt.hist(FareDist, log = 1)
plt.title("Fare Distribution")

plt.savefig("./../Histograms/Fare.png")
plt.close()

#######################################################


nan_count = df.isna().sum()
cols_missing_vals = df.columns[df.isnull().any()]

for i in range(0,len(cols_missing_vals)):
    print("{:.2f}".format(nan_count[cols_missing_vals[i]] / num_rows * 100),"% din datele din col", cols_missing_vals[i], "lipsesc")
print("\n")

######

df_survived = df[df['Survived'] == 1]
nan_count = df_survived.isna().sum()
cols_missing_vals = df_survived.columns[df_survived.isnull().any()]

for i in range(0,len(cols_missing_vals)):
    print("{:.2f}".format(nan_count[cols_missing_vals[i]] / num_rows * 100),"% din datele din col", cols_missing_vals[i], "lipsesc in cazul pasagerilor ce au supravietiuit")
print("\n")
#####

df_dead = df[df['Survived'] == 0]
nan_count = df_dead.isna().sum()
cols_missing_vals = df_survived.columns[df_dead.isnull().any()]

for i in range(0,len(cols_missing_vals)):
    print("{:.2f}".format(nan_count[cols_missing_vals[i]] / num_rows * 100),"% din datele din col", cols_missing_vals[i], "lipsesc in cazul pasagerilor ce NU au supravietiuit")
print("\n")

####################################


df_0_20 = df[df['Age'] <= 20]

df_21_40 = df[df['Age'] <= 40]
df_21_40 = df_21_40[df_21_40['Age'] >= 21]

df_41_60 = df[df['Age'] <= 60]
df_41_60 = df_41_60[df_41_60['Age'] >= 41]

df_61plus = df[df['Age'] >= 61]

print(len(df_0_20), len(df_21_40), len(df_41_60), len(df_61plus))

nan_count = df.isna().sum()
print(nan_count['Age'])


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


a = df['AgeGroup'].value_counts()[1] / num_rows * 100
b = df['AgeGroup'].value_counts()[2] / num_rows * 100
c = df['AgeGroup'].value_counts()[3] / num_rows * 100
d = df['AgeGroup'].value_counts()[4] / num_rows * 100

unknown = 100 - a - b - c - d
x = np.array([a, b, c, d, unknown])
mylabels = ["[0-20]", "[21-40]", "[41-60]", "61+", "Nan"]
plt.pie(x, autopct='%1.1f%%', labels = mylabels)
plt.title('Distribution between ages')

plt.savefig("C5.png")
plt.close()

# df['Survived'].value_counts()[0]
print('\n')

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

plt.savefig("C6.png")
plt.close()
