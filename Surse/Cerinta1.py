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

plt.savefig("./../Histograms/ageDist.png")
plt.close()

############

SurvivedDist = df['Survived'].values.tolist()
plt.hist(SurvivedDist, bins=[0, 0.5, 1], label = "hop")
plt.title("Survival Distribution")


plt.savefig("./../Histograms/SurvivalDist.png")
plt.close()

###############

PclassDist = df['Pclass'].values.tolist()
plt.hist(PclassDist, bins=3)
plt.title("Pclass Distribution")

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

plt.savefig("C5.png")
plt.close()
