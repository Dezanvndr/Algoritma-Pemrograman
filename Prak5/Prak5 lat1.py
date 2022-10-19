# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 09:40:36 2022
@Materi: Control Structure Exercise
@Judul: Praktikum 5 Latihan 1
@Hari/Tanggal: Rabu, 19 10 22
@NIM: 064001600031
@author: dezan
"""

n = '0'
total = 0
tampung = 0

while (n != ''):
   n = str(input('masukkan nilai: '))
   n = n.upper()
   tampung += 1
   if(n == ''):
       break;
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
       print("masukkan nilai yang benar, input anda salah")

if(tampung == 1):
    print("rata - rata nya adalah: 0")
else:
    rerata = total/(tampung-1)
    print ("rata - rata nya adalah: ", rerata)