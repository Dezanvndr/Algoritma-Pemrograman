# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 10:34:54 2022

@author: dezan
"""

print("Hitung Luas Ruangan")

panjang = float(input("Masukkan Panjang Ruangan: "))
lebar = float(input("Masukkan Lebar Ruangan: "))
satuan = input("Masukkan Satuan (Meter/Inci): ")

hasil = panjang * lebar

print("Luas ruangan dengan panjang ", panjang, " dan lebar ", lebar, " adalah ", hasil, " ", satuan)