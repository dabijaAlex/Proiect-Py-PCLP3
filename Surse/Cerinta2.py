#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
num_rows = len(df)

fig, axs = plt.subplots(1, 3)

print("\n--------------------------------------------------\n")
print("procent pers ce au supravietuit = ", round(df['Survived'].value_counts()[1] / num_rows * 100, 2), "%")
print("procent pers ce au NU supravietuit = ", round(df['Survived'].value_counts()[0] / num_rows * 100, 2), "%")
print("\n--------------------------------------------------\n")
x = np.array([df['Survived'].value_counts()[1] / num_rows * 100, df['Survived'].value_counts()[0] / num_rows * 100])
mylabels = ["Survived", "Not Survived"]
axs[0].pie(x, autopct='%1.2f%%', labels = mylabels)

y = np.array([df['Pclass'].value_counts()[1] / num_rows * 100, df['Pclass'].value_counts()[2] / num_rows * 100, df['Pclass'].value_counts()[3] / num_rows * 100])
mylabels_class = ["First Class", "Sec Class", "Third Class"]
axs[1].pie(y, autopct='%1.1f%%', labels = mylabels_class)

print("procent pers clasa 1 = ", round(df['Pclass'].value_counts()[1] / num_rows * 100, 2), "%")
print("procent pers clasa 2 = ", round(df['Pclass'].value_counts()[2] / num_rows * 100, 2), "%")
print("procent pers clasa 3 = ", round(df['Pclass'].value_counts()[3] / num_rows * 100, 2), "%")
print("\n--------------------------------------------------\n")

z = np.array([df['Sex'].value_counts()['male'] / num_rows * 100, df['Sex'].value_counts()['female'] / num_rows * 100])
mylabels_gender = ["Male", "Female"]
axs[2].pie(z, autopct='%1.2f%%', labels = mylabels_gender)

print("procent barbati = ", round(df['Sex'].value_counts()['male'] / num_rows * 100, 2), "%")
print("procent femei = ", round(df['Sex'].value_counts()['female'] / num_rows * 100, 2), "%")
print("\n--------------------------------------------------\n")


plt.tight_layout()
plt.title("Survival rates / Distribution among classes / Gender distribution                                                                              ")
plt.savefig("../Images/C2.png")
plt.close()