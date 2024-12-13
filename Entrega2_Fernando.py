# -*- coding: utf-8 -*-
"""execicio1 numpy.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G-i_COSCpoDBqdBttiJINrnDbgbiauZ3

Você foi contratado (a) para analisar os dados de produção de uma fábrica que fabrica três produtos diferentes. A cada semana, a fábrica gera um relatório com a produção de cada produto, e seu objetivo é analisar e manipular esses dados usando Numpy. A fábrica quer simular os dados de produção de 6 semanas para três produtos (A, B, C). Cada produto tem uma produção aleatória entre 50 e 150 unidades por semana.
Use a função np.random.randint para criar uma matriz 6x3 (6 semanas, 3 produtos) com os valores de produção para cada semana.
Agora que você tem os dados de produção, faça os seguintes cálculos: Calcule a média de produção de cada produto (A, B e C) ao longo das 6 semanas. Descubra em qual semana houve a maior produção total (soma de todos os produtos).

Após análise, a fábrica decidiu aumentar a produção dos produtos A e C em 20% e reduzir a produção do produto B em 10%.
Atualize os valores na matriz de produção para refletir esse ajuste.
Transposição e Operações Matriciais (para uma melhor visualização, a fábrica quer ver os dados transpostos)
Transponha a matriz de produção para que as semanas sejam representadas em colunas e os produtos em linhas.
"""

import numpy as np

import numpy as np


produtoA = np.random.randint(50, 150, size=(6, 3))
produtoB = np.random.randint(50, 150, size=(6, 3))
produtoC = np.random.randint(50, 150, size=(6, 3))

maior_valorvendasA = np.max(produtoA)
maior_valorvendasB = np.max(produtoB)
maior_valorvendasC = np.max(produtoC)

mediaA = np.mean(produtoA, axis=0)
mediaB = np.mean(produtoB, axis=0)
mediaC = np.mean(produtoC, axis=0)

semana_maior_producao = np.argmax(produtoA + produtoB + produtoC, axis=0)

reajusteA = produtoA * 1.2
reajusteB = produtoB * 0.9
reajusteC = produtoC * 1.2


produtoA_transposto = produtoA.T
produtoB_transposto = produtoB.T
produtoC_transposto = produtoC.T

print(f'Produto A:\n {produtoA}')
print(f'\nProduto B:\n {produtoB}')
print(f'\nProduto C:\n {produtoC}')

print(f'\nO maior valor de vendas do produto A é: {maior_valorvendasA:.2f}')
print(f'\nO maior valor de vendas do produto B é: {maior_valorvendasB:.2f}')
print(f'\nO maior valor de vendas do produto C é: {maior_valorvendasC:.2f}')


print("\n\nMédia de produção de cada produto (A, B, C) ao longo das 6 semanas:")
print(f'\nProduto A: {np.round(mediaA,2)}')
print(f'\nProduto B: {np.round(mediaB,2)}')
print(f'\nProduto C: {np.round(mediaC,2)}')

print(f"\nSemana com maior produção total: {np.round(semana_maior_producao,2)}")

print("\nMatriz de produção reajustada:")
print("\nProduto A após reajuste:")
print(np.round(reajusteA,2))
print("\nProduto B após reajuste:")
print(np.round(reajusteB,2))
print("\nProduto C após reajuste:")
print(np.round(reajusteC,2))

print("\nMatriz transposta de produção:")
print("\nProduto A transposto:")
print(produtoA_transposto)
print("\nProduto B transposto:")
print(produtoB_transposto)
print("\nProduto C transposto:")
print(produtoC_transposto)