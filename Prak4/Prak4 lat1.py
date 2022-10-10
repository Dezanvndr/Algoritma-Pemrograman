# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 10:11:17 2022

@author: dezan
"""

# Versi 1
a = int(input("masukkan jumlah maksimal: "))
for i in range(a, 0, -1):
    print(i)
    for j in range(0, i):
        print(i, end='')
    print()

# Versi 2
a = int(input("masukkan jumlah maksimal: "))
for i in range(-1, a):
    for j in range(-1, a - 1):
        print(a , end='')
    a -= 1
    print('')
     