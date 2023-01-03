# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 09:00:48 2023

@author: dezan
"""

import pandas as pd

data = {"Negara": ["Indonesia", "Jepang", "India", "China", "Amerika Serikat", "Brazil", "Rusia"],
        "Ibu Kota": ["Jakarta", "Tokyo", "New Delhi", "Beijing", "Washington DC", "Brazilia", "Moskow"],
        "Benua": ["Asia", "Asia", "Asia", "Asia", "Amerika", "Amerika", "Asia"],
        "Luas": [1905, 377, 3287, 9597, 9834, 8515, 17098],
        "Populasi": [264, 143, 1252, 1357, 329, 210, 146] }

df = pd.DataFrame(data)
mean = df.groupby(['Benua']).mean()
std = df.groupby(['Benua']).std()

print(df)
print(mean)
print(std)

