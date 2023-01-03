# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 08:45:58 2023

@author: dezan
"""

def tukar(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def bubbleSort(A, n):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            tukar(A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)

A = [3, 5, 8, 4, 1, 9, -2]
bubbleSort(A, len(A))
print("List yang sudah disorting")
print(A)