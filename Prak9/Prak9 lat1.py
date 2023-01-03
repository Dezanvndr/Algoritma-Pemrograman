# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 08:27:48 2023

@author: dezan
"""

def writeFile():
    inputNama = input("Masukkan Nama mu: ")
    inputUmur = input("Masukkan Umur mu: ")
    inputAlamat = input("Masukkan Alamatmu: ")
    inputEmail = input("Masukkan Emailmu: ")
    inputDosen = input("Masukkan Dosen Walimu: ")
    
    # Create & Write File
    fileWrite = open("Biodata.txt", "w")
    fileWrite.write("Nama: " + inputNama + "\nUmur: " + inputUmur + "\nAlamat: " + inputAlamat + "\nEmail: " + inputEmail + "\nDosen Wali: " + inputDosen)
    fileWrite.close()

def readFile():
    # Read File
    fileRead = open("Biodata.txt", "r")
    text = fileRead.read()
    print("Berikut Ini Data Kamu")
    print(text)
    fileRead.close()

writeFile()
print("\n")
readFile()