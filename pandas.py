# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V-gY95NEwkaBHaMHEmReK1S9ekoLeAkT
"""

import pandas as pd
import numpy as np

s1=pd.Series([1,2,-5,0])

s1

s1.values

s1.index

s9=pd.Series(['onix','gol'], index=['gm','vw'])

s9

s2=pd.Series([1,2,-5,0], index=['amarelo','b','c','d'])

s2

s2['amarelo']=1000

s2.index

s2

s2[s2>0]

s2*2

s2.isnull()

s2

dados={'estado':['SP','MG','PR','SP','MG','PR'], #Criando o conjunto de Dados para o DataFrame
       'ano':[2019,2019,2019,2024,2024,2024],
       'pop':[45.9,17.3,16.9,46.6,21.4,18.3]}

df1=pd.DataFrame(dados) #Criando o DataFrame

df1

df1.head(2) #Mostra as duas primeiras linhas do seu DataFrame

df1.tail(2) #Mostra as duas últimas linhas do seu DataFrame

df1.sample(2) #Sample vai pegar amostras aleatórias do DataFrame

df2=pd.DataFrame(dados,columns=['ano','estado','pop']) #Clona o DF1, Recriando o df1, através do df2 (é uma ´cópia por segurança)

df2

df2['estado'] #Apresenta apenas a coluna Estado

df2.ano #Apresenta apenas a coluna Ano

df2.dtypes

df2['estimativa']=50 #Cria uma outra coluna

df2

df2['estimativa'] = np.arange(6) #pega um valor ordenado, de 0 a 5

df2

df2['Não Paraná']=df2.estado!='PR' #Cria uma nova coluna colocando falso para Paraná

df2

del df2['Não Paraná'] #Deleta a coluna não paraná

df2

df2.shape #Retorna a quantidade de linhas e colunas

df2.columns=['Ano','Estado','População','Estimativa'] #Renomeia as colunas

df2

df2.describe(include='all') #Retorna um resumo estatístico do DataFrame (NaN not a number)(std desvio padrao)

df2.drop([0,1]) #ATENÇÂO CUIDADO, exclui a linha permanentemente

df2.iloc[0] #Seleciona expecificamente uma coluna, no caso a 0

df2.iloc[1:3] #Seleciona um intervalo de linhas, no caso a linha 1 e 2

dados2.pd.read_csv('Teste.csv') #Lendo um arquivo CSV externo (tres barras > fazer upload > seleciona aruivo)

df3=pd.DataFrame(dados2) #criando o DataFrame do arquivo de dados selecionados

df3.head(2) #selecionando as duas primeiras linhas, para testar