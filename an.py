import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Ler o arquivo
df = pd.read_csv("dataset1.csv", sep=";")
#Mostra tudo
pd.set_option('display.max_rows', None)
#Testes
df['US 2024 Deficit'] = pd.to_numeric(df['US 2024 Deficit'], errors='coerce')


print(df[['US 2024 Deficit']] > 30)
