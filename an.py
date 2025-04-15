import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Ler o arquivo
df = pd.read_csv("dataset1.csv", sep=";")

#Mostra tudo
pd.set_option('display.max_rows', None)

#Testes
df['US 2024 Deficit'] = df['US 2024 Deficit'].str.replace(",", "").astype(float)

print(df[df['US 2024 Deficit'] < -30])
