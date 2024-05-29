import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
num_rows = len(df)

def get_title_from_name(name):
    if 'Mr.' in name:
        return 'Mr.'
    if 'Mrs.' in name:
        return 'Mrs.'
    if 'Ms.' in name:
        return 'Ms.'
    if 'Don' in name:
        return 'Don'
    if 'Dr.' in name:
        return 'Dr.'
    if 'Miss.' in name:
        return 'Miss.'
    if 'Master.' in name:
        return 'Master.'
    if 'Jonkheer.' in name:
        return 'Jonkheer.'
    if 'Rev.' in name:
        return 'Rev.'
    if 'Mlle.' in name:
        return 'Mlle'
    if 'Countess' in name:
        return 'Countess'
    if 'Capt.' in name:
        return 'Capt.'
    if 'Mme.' in name:
        return 'Mme.'
    if 'Major.' in name:
        return 'Major.'
    if 'Lady.' in name:
        return 'Lady'
    if 'Col.' in name:
        return 'Col'
    if 'Sir.' in name:
        return 'Sir.'
    return None
pass

df['Title'] = df['Name'].apply(get_title_from_name)


title_counts = df['Title'].value_counts()
mylabels = df['Title'].value_counts().index
bars = plt.bar(mylabels, title_counts)
plt.xticks(rotation = 35) # altfel nu se vad alea calumea pe axa x
plt.autoscale(enable = True, tight=True, axis = 'y')
plt.xlabel('Titlu')
plt.ylabel('Număr de persoane')
plt.title('Numărul de persoane pentru fiecare titlu')
plt.bar_label(bars)
plt.savefig("../Images/C9.png")
plt.close()

df.to_csv('new_df_C9.csv', index = True)