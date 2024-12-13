# -*- coding: utf-8 -*-
"""Untitled28.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K03NLqppCERWKVl3n0WknW3VtyIl0LCs
"""

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

produtos = pd.Series(['Eletrônicos', 'Roupas', 'Alimentos', 'Móveis'])

ultimo_tri = pd.date_range(start='2024-10-01', end='2024-12-31', freq='W')

semanas = [f'Semana {i}' for i in range(1, 13)]

np.random.seed(42)

vendas = pd.DataFrame(np.random.randint(1000, 10000, size=(len(semanas), len(produtos))),
                      columns=produtos,
                      index=semanas)

vendas_media = vendas.mean()

semana_maior_receita = vendas.sum(axis=1).idxmax()

categoria_maior_venda = vendas.sum().idxmax()

vendas['Eletrônicos'] *= 1.25
vendas['Móveis'] *= 1.10
vendas['Roupas'] *= 0.70

vendas_atualizada = vendas

vendas_atualizada = pd.DataFrame(vendas_atualizada)

ultimo_tri = pd.date_range(start='2024-10-01', end='2024-12-31', freq='W')

figure, ax = plt.subplots(figsize=(13, 8))
vendas_atualizada = sns.lineplot(data=vendas_atualizada)
plt.show()