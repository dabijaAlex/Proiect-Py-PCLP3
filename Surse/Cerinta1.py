#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


df = pd.read_csv('train.csv')

num_cols = len(df.columns)
print("nr coloane = ", num_cols)
print("---------------------")
print("TYPE PT FIECARE COLOANA:\n")
print(df.dtypes)

print("---------------------")
nan_count = df.isna().sum()
print("NR DATE LIPSA PT FIECARE COLOANA:\n")
print(nan_count)
print("---------------------")
num_rows = len(df)
print("nr linii = ", num_rows)
print("---------------------")

if (df.duplicated().sum()):
    print("there are some duplicates\n")
else:
    print("no duplicates\n")