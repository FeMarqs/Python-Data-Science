# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IA8G49Yrs8QuK8B6ohP3xvJllgS-d7i6
"""



"""Exercícios de Fixação

Faça um algoritmo que receba um valor de uma compra e receba o número de prestações, apresente o valor das prestações sem juros.
"""

# Recebe o valor da compra
valor_compra = float(input("Digite o valor da compra: R$ "))

# Recebe o número de prestações
num_prestacoes = int(input("Digite o número de prestações: "))

# Calcula o valor total com o acréscimo de 5% de juros
valor_total_com_juros = valor_compra * 1.05  # 5% de acréscimo

# Calcula o valor de cada prestação com o acréscimo de juros
valor_prestacao_com_juros = valor_total_com_juros / num_prestacoes

# Exibe o valor das prestações com juros
print(f"O valor total da compra com 5% de juros é: R$ {valor_total_com_juros:.2f}")
print(f"O valor de cada prestação com 5% de juros é: R$ {valor_prestacao_com_juros:.2f}")