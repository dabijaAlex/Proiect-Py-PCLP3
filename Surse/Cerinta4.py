import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
num_rows = len(df)


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