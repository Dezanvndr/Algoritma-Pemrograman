# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 08:58:07 2022

@author: dezan
"""

#Versi 1
def Prima(x):
    if x <= 1:
        return False
    for i in range (2, x):
        if x % i == 0:
            return False
    return True

def Main():
    angka = int(input("Masukkan angka: "))
    if Prima(angka):
        print (angka, "adalah bilangan Prima")
    else:
        print (angka, "bukanlah bilangan Prima")
        
Main()

#Versi 2
def prima(angka):
    for i in range(2, angka):
        if (angka % i) ==  0:
            return print (angka, "bukan bilangan prima\n", i, "kali", angka//i, "=", angka)
        else:
            return print (angka, "adalah bilangan prima")

def notprima(angka):
    if angka > 1:
        prima(angka)
    else:
        print (angka, "bukan bilangan prima")

angka = int(input("masukkan bilangan: "))
notprima(angka)