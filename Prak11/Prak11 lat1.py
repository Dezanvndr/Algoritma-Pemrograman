# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 08:53:38 2023

@author: dezan
"""

class Mahasiswa:
   mhsCount = 0

   def __init__(self, name, nim, angkatan):
      self.name = name
      self.nim = nim
      self.angkatan = angkatan
      Mahasiswa.mhsCount += 1
   
   def displayCount(self):
     print ("Total Mahasiswa %d" % Mahasiswa.mhsCount)

   def displayMahasiswa(self):
      print("Nama: ", self.name)
      print("Nim: ", self.nim)
      print("Angkatan: ", self.angkatan)


nama = input("Masukkan Namamu: ")
nim = input("Masukkan NIM kamu: ")
angkatan = input("Masukkan Tahun Angkatanmu: ")

print("\n")
mhs1 = Mahasiswa(nama, nim, angkatan)
mhs1.displayMahasiswa()

print("\n")
print ("Total Mahasiswa %d" % Mahasiswa.mhsCount)