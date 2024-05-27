#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


df = pd.read_csv('test.csv')
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



nr_copii = df[(df['Age'] < 18)].shape[0]
nr_copii_suprav = df[(df['Age'] < 18) & (df['Survived'] == 1)].shape[0]
print("copii = ",nr_copii)
print("nr copii suprav = ", nr_copii_suprav)
a = nr_copii_suprav / nr_copii * 100
nr_adulti = df[(df['Age'] >= 18)].shape[0]
nr_adulti_suprav = df[(df['Age'] >= 18) & (df['Survived'] == 1)].shape[0]
print(nr_adulti, nr_adulti_suprav)
b = nr_adulti_suprav / nr_adulti * 100

x = ([a , b])
mylabels = ["copii", "adulti"]
bars = plt.bar(mylabels, x)
plt.title("% of kids that surv from nr of kids vs of adults that surv from nr of adults")
plt.ylabel('Percentages', fontsize = 12)
plt.bar_label(bars)

plt.savefig("C7.png")
plt.close()

df_to_complete = pd.read_csv('test.csv')

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
df_to_complete.to_csv('new_df.csv', index = True)
#intreaba daca trebuie sa cureti datele cu NA

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
plt.savefig("C9.png")
plt.close()




df['alone'] = (df['SibSp'] + df['Parch'] == 0)

alone_survived = df.groupby(['alone', 'Survived']).size().unstack().fillna(0)

alone_survived.plot(kind='bar', stacked=True, ax=plt.gca(), rot = True)
plt.ylabel('Număr de persoane')
plt.title('Influența stării de a fi singur pe Titanic asupra șanselor de supraviețuire')
plt.xticks([0, 1], ['Impreuna', 'Singur'])
plt.legend(['Nu a supraviețuit', 'A supraviețuit'])
plt.savefig("C10.png")
plt.close()



sns.catplot(data=df.head(100), x='Pclass', y='Fare', hue='Survived', kind='swarm', height=4, aspect=2, s=14)
plt.xlabel('Clasă')
plt.ylabel('Tarif')

plt.savefig("C10_part2.png")
plt.close()
