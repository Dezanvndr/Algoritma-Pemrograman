# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:15:15 2023

@author: dezan
"""

import pandas as pd

df = pd.read_csv('Negara.csv', index_col=0)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print("Berikut Data Framenya:")
print(df, "\n")

print("Berikut Data Mean:")
print(mean, "\n")

print("Berikut Data Standard Deviation:")
print(std, "\n")

mean.to_csv('NegaraMean.csv')
std.to_csv('NegaraStandarDeviasi.csv')
print("File Berhasil Dibuat")