import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df_to_complete = pd.read_csv('train.csv')

x = (df_to_complete[(df_to_complete['Survived'] == 1)])["Age"].mean()
x = int(x)
df_to_complete.loc[df_to_complete['Survived'] == 1, 'Age'] = x

x = (df_to_complete[(df_to_complete['Survived'] == 0)])["Age"].mean()
x = int(x)
df_to_complete.loc[df_to_complete['Survived'] == 0, 'Age'] = x


x = (df_to_complete[(df_to_complete['Survived'] == 1)])['Embarked'].mode()
df_to_complete.loc[df_to_complete['Survived'] == 1, 'Embarked'] = x[0]

x = (df_to_complete[(df_to_complete['Survived'] == 0)])['Embarked'].mode()
df_to_complete.loc[df_to_complete['Survived'] == 0, 'Embarked'] = x[0]


print(df_to_complete.head(10))
nan_count = df_to_complete.isna().sum()
print(nan_count)
df_to_complete.to_csv('new_df_C8.csv', index = True)