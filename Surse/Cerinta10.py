import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_csv('train.csv')
num_rows = len(df)


df['alone'] = (df['SibSp'] + df['Parch'] == 0)

alone_survived = df.groupby(['alone', 'Survived']).size().unstack().fillna(0)

alone_survived.plot(kind='bar', stacked=True, ax=plt.gca(), rot = True)
plt.ylabel('Număr de persoane')
plt.title('Influența stării de a fi singur pe Titanic asupra șanselor de supraviețuire')
plt.xticks([0, 1], ['Impreuna', 'Singur'])
plt.legend(['Nu a supraviețuit', 'A supraviețuit'])
plt.savefig("../Images/C10.png")
plt.close()



sns.catplot(data=df.head(100), x='Pclass', y='Fare', hue='Survived', kind='swarm', height=4, aspect=2, s=14)
plt.xlabel('Clasă')
plt.ylabel('Tarif')

plt.savefig("../Images/C10_part2.png")
plt.close()
