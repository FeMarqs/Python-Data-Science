# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b9BHqnGjSnm4prbh2XR-GlYOHQlmoRb5
"""

import statistics
import math as mt

#definindo nosso conjunto de dados(pode ser uma lista de númoeros
media = [1,2,3,4,5,7]

final = statistics.mean(media)

print(final)

final2 = statistics.median(media)

print(final2)

final3 = statistics.median_high(media)

print(final3)

final4 = statistics.median_low(media)

print(final4)