import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')

ageDist = df['Age'].values.tolist()
plt.hist(ageDist)
plt.title("Age Distribution")
plt.ylabel('number of people', fontsize = 12)
plt.xlabel('Ages', fontsize = 12)

plt.savefig("./../Histograms/ageDist.png")
plt.close()

############


mylabels = df['Survived'].value_counts().index
x = df['Survived'].value_counts()
mylabels = ["Dead", "Survived"]
bars = plt.bar(mylabels, x)
plt.title("Survival Distribution")
plt.ylabel('number of people', fontsize = 12)
plt.bar_label(bars)
# plt.xticks([])

plt.savefig("./../Histograms/SurvivalDist.png")
plt.close()

###############

x = df['Pclass'].value_counts()
mylabels = ["1", "2", "3"]
bars = plt.bar(mylabels, x)
plt.ylabel('number of people', fontsize = 12)
plt.xlabel('Class', fontsize = 12)
plt.title("Pclass Distribution")
plt.bar_label(bars)



plt.savefig("./../Histograms/Pclass.png")
plt.close()


#############
x = df['SibSp'].value_counts()
mylabels = df['SibSp'].value_counts().index
bars = plt.bar(mylabels, x)
plt.title("SibSp Distribution")
plt.ylabel('number of people', fontsize = 12)
plt.bar_label(bars)

plt.savefig("./../Histograms/SibSp.png")
plt.close()


##############

x = df['Parch'].value_counts()
mylabels = df['Parch'].value_counts().index
bars = plt.bar(mylabels, x)
plt.title("Parch Distribution")
plt.ylabel('number of people', fontsize = 12)
plt.bar_label(bars)


plt.savefig("./../Histograms/Parch.png")
plt.close()

###########

# FareDist = df['Fare'].values.tolist()
bars = plt.hist(df['Fare'], [0, 30, 60, 100, 200, 300, 500, 1000])
plt.title("Fare Distribution")

plt.savefig("./../Histograms/Fare.png")
plt.close()