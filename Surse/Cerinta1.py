#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


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
    print("there are some duplicates\n")
else:
    print("no duplicates\n")