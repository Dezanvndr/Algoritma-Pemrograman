# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 14:34:17 2022

@author: dezan
"""

def kategori(n = "0", total = 0, tampung = 0):
    while (n != ''):
        n = str(input('masukkan nilai: '))
        tampung += 1
        n.upper()
        if(n == ''):
            if(tampung == 1):
                return 0
            else:
                return total/(tampung - 1)
        elif (n == 'A'):
            print('nilai = 4')
            total += 4
        elif (n == 'A-'):
            print('nilai = 3.75')
            total += 3.75
        elif (n == 'B+'):
            print('nilai = 3.5')
            total += 3.5
        elif (n == 'B'):
            print('nilai = 3')
            total += 3
        elif (n == 'B-'):
            print('nilai = 2.75')
            total += 2.75
        elif (n == 'C+'):
            print('nilai = 2.5')
            total += 2.5
        elif (n == 'C'):
            print('nilai = 2')
            total += 2
        elif (n == 'C-'):
            print('nilai = 1.75')
            total += 1.75
        elif (n == 'D'):
            print('nilai = 1.5')
            total += 1.5
        elif (n == 'E'):
            print('nilai = 1.25')
            total += 1.25
        else:
            tampung -= 1
            print("masukkan nilai yang benar")
    
rerata = kategori()
print ("Rata-ratanya adalah: ", rerata)
