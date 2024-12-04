# -*- coding: utf-8 -*-
"""MediaMelhorTempoAtleta.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1p36mtFy5JVVvsnldWg8g2HrpuVGSn7e-

1 - Suponha que você está analisando o desempenho de uma atleta em cinco corridas diferentes. Os tempos (em minutos) que o atleta levou para completar cada corrida são os seguintes: [10, 15, 20, 25, 30]

Você deseja calcular:
a) o tempo médio que o atleta levou para completar as corridas.
b) melhor tempo
"""

import statistics as st

tempo = [10, 15,20, 25, 30]

media = st.mean(tempo)

melhor_tempo = min(tempo)

print(f'O tempo médio que o atleta levou para completar as corridas é de {media} minutos')

print(f'O melhor tempo que o atleta levou para completar as corridas é de {melhor_tempo} minutos')