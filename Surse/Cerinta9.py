import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
num_rows = len(df)

def extract_title(name):
    if 'Mr.' in name:
        return 'Mr.'
    elif 'Mrs.' in name:
        return 'Mrs.'
    elif 'Ms.' in name:
        return 'Ms.'
    elif 'Don' in name:
        return 'Don'
    elif 'Dr.' in name:
        return 'Dr.'
    elif 'Miss.' in name:
        return 'Miss.'
    elif 'Master.' in name:
        return 'Master.'
    elif 'Jonkheer.' in name:
        return 'Jonkheer.'
    elif 'Rev.' in name:
        return 'Rev.'
    elif 'Mlle.' in name:
        return 'Mlle'
    elif 'Countess' in name:
        return 'Countess'
    elif 'Capt.' in name:
        return 'Capt.'
    elif 'Mme.' in name:
        return 'Mme.'
    elif 'Major.' in name:
        return 'Major.'
    elif 'Lady.' in name:
        return 'Lady'
    elif 'Col.' in name:
        return 'Col'
    elif 'Sir.' in name:
        return 'Sir.'
    else: return "unknown"

def check_title_sex(title, sex):
    male_titles = ['Mr.', 'Don', 'Master.', 'Rev.', 'Col.', 'Capt.', 'Major.', 'Sir.']
    female_titles = ['Mrs.', 'Ms.', 'Miss.', 'Mlle', 'Countess', 'Mme.', 'Lady']
    if title in male_titles and sex == 'male':
        return True
    elif title in female_titles and sex == 'female':
        return True
    elif title == 'Dr.':
        return True
    elif title == 'Jonkheer.':
        return True
    else:
        return False

df['Title'] = df['Name'].apply(extract_title)

df['Title_Valid'] = df.apply(lambda row: check_title_sex(row['Title'], row['Sex']), axis=1)

title_counts = (df[(df['Title_Valid'] == True)])['Title'].value_counts()
mylabels = (df[(df['Title_Valid'] == True)])['Title'].value_counts().index
bars = plt.bar(mylabels, title_counts)
plt.xticks(rotation = 35)
plt.autoscale(enable = True, tight=True, axis = 'y')
plt.xlabel('Titlu')
plt.ylabel('Număr de persoane')
plt.title('Numărul de persoane pentru fiecare titlu')
plt.bar_label(bars)
plt.savefig("../Images/C9.png")
plt.close()

df.to_csv('new_df_C9.csv', index = True)