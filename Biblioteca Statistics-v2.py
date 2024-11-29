# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Jw057v5_Yy1qhcLCMd8ZIs_Cu0I7NFYU
"""

#Importando a biblioteca necessária para lidar com estatísticas
import statistics as st #st foi um apelido dado para facilitar, assim como final1, final2, final3...
import math as mt #mt também foi um apelido

#definindo nosso conjunto de dados (pode ser uma lista de números)
dados = [10, 15, 20, 25, 30, 35, 40, 50]

#calculando a média
media = st.mean(dados)

#calculando a mediana
mediana = st.median(dados)

#calculando a moda
moda = st.mode(dados)

#Exibindo os resultados
print("Conjunto de dados:", dados)

print("Média:", media)

print("Mediana:", mediana)

print("Moda:", moda)