# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 12:20:04 2022

@author: dezan
"""

import math

t1 = float(input("masukkan lattitude kota pertama = "))
g1 = float(input("masukkan longitude kota pertama = "))

t2 = float(input("masukkan lattitude kota kedua = "))
g2 = float(input("masukkan longitude kota kedua = "))

dlat = t2 - t1
dlon = g2 - g1

a = math.sin(math.radians(dlat/2)) ** 2 + math.cos(math.radians(t1)) * math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) ** 2

# Versi Arc sinus
c = 2 * math.asin(math.sqrt(a))

# Versi Arc tangen 2
#c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
r = 6371.01

print("jarak antara dua titik adalah" , c*r , "kilometer")