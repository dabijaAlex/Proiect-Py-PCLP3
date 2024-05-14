#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# def has_duplicate_lines():
#     with open("train.csv", 'r') as file:
#         lines = file.readlines()
#         unique_lines = set(lines)
#     return len(unique_lines) != len(lines)


# def format_line(line):
#     line = line.strip('\n')
#     list_of_line = line.split(',')
#     merged_elem = list_of_line[3] + "," + list_of_line[4]
#     list_of_line[3:5] = [merged_elem]
#     return list_of_line
#     pass

# def check_type(element):

#     tip = "string"

#     try:
#         float(element)
#         tip = "float"
#     except ValueError:
#         pass

#     try:
#         int(element)
#         tip = "int"
#     except ValueError:
#         pass

#     return tip

# def get_types_for_each(list_of_line, tipuri_pt_col):
#     for i in range(len(list_of_line)):
#         if list_of_line[i] != '':
#             type_of_data = check_type(list_of_line[i])
#             tipuri_pt_col[cols[i]] = type_of_data
#     return tipuri_pt_col

# def count_nr_elems_each_col(list_of_line, nr_elem_pe_col):
#     for i in range(len(list_of_line)):
#         if list_of_line[i] != '':
#             nr_elem_pe_col[i] += 1
#     return nr_elem_pe_col

# f = open('train.csv', 'r')

# #numaram coloaneale
# line = f.readline()
# line = line.strip('\n')

# cols = line.split(',')
# nr_coloane = len(cols)
# print("nr coloane = ", nr_coloane)


# tipuri_pt_col = {}
# for i in cols:
#     tipuri_pt_col[i] = "default"

# nr_lines = 0
# nr_elem_lipsa_pe_col = [0] * 12
# line = f.readline()

# while line:
#     nr_lines += 1
#     list_of_line = format_line(line)
#     tipuri_pt_col = get_types_for_each(list_of_line, tipuri_pt_col)

#     nr_elem_lipsa_pe_col = count_nr_elems_each_col(list_of_line, nr_elem_lipsa_pe_col)

#     line = f.readline()

# print(tipuri_pt_col)

# for i in range(len(nr_elem_lipsa_pe_col)):
#     nr_elem_lipsa_pe_col[i] = nr_lines - nr_elem_lipsa_pe_col[i]
# print(nr_elem_lipsa_pe_col)

# print("nr linii = ", nr_lines)

# print("Does the file have dupes ?", has_duplicate_lines())
# f.close()

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
    print("there are some duplicates")
else:
    print("no duplicates")

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

plt.savefig("img.png")
