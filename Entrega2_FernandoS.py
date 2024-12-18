# -*- coding: utf-8 -*-
"""Untitled27.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1s45S_YdhbEydqdqnWsXv1R-6jbf3I924
"""

import numpy as np

import numpy as np


prodA = np.random.randint(10, 1000, size=(6, 3))
prodB = np.random.randint(10, 1000, size=(6, 3))
prodC = np.random.randint(10, 1000, size=(6, 3))

maior_valvendA = np.max(prodA)
maior_valvendB = np.max(prodB)
maior_valvendC = np.max(prodC)



medA = np.mean(prodA, axis=0)
medB = np.mean(prodB, axis=0)
medC = np.mean(prodC, axis=0)

print(f'Produto A:\n {prodA}')
print(f'\nProduto B:\n {prodB}')
print(f'\nProduto C:\n {prodC}')

sem_maior_prod = np.argmax(prodA + prodB + prodC, axis=0)

reajA = prodA * 1.2
reajB = prodB * 0.9
reajC = prodC * 1.2


prodA_transp = prodA.T
prodB_transp = prodB.T
prodC_transp = prodC.T



print(f'\nVendas do produto A é: {maior_valvendA:.2f}')
print(f'\nVendas do produto B é: {maior_valvendB:.2f}')
print(f'\nVendas do produto C é: {maior_valvendC:.2f}')


print("\n\nMédia de produção de cada produto (A, B, C) ao longo das 6 semanas:")
print(f'\nProduto A: {np.round(medA,2)}')
print(f'\nProduto B: {np.round(medB,2)}')
print(f'\nProduto C: {np.round(medC,2)}')

print(f"\nSemana com maior produção total: {np.round(sem_maior_prod,2)}")

print("\nCom reajuste:")
print("\nProduto A:")
print(np.round(reajA,2))
print("\nProduto B:")
print(np.round(reajB,2))
print("\nProduto C:")
print(np.round(reajC,2))

print("\nMatriz Transposta:")
print("\nTransposto A:")
print(prodA_transp)
print("\nTransposto B:")
print(prodB_transp)
print("\nTransposto C:")
print(prodC_transp)