import pandas as pd
import datetime
import numpy as np

# Importando módulos personalizados para limpeza e transformação dos dados
import dataclean
import transform

# Carregando o dataset a partir de um arquivo CSV do Git
# Define a primeira coluna como índice ao carregar os dados


df = pd.read_csv(
    "https://raw.githubusercontent.com/JackyP/testing/master/datasets/nycflights.csv",
    index_col=0
)

# Aplicando a função de limpeza de dados do módulo dataclean
# Invocando a função retira_vazio dataclean.py

df_work = dataclean.retira_vazio(df)

# Calculando o tempo de voo em horas e adicionando ao DataFrame
# Invocando a função calc_horas do tranform.py
transform.calc_horas(df_work, "tempo_voo")

# Classificando os voos por turno com base na hora do voo
# Invocando a função classifica_turno do tranform.py
df_work['classificacao'] = df_work['data_hora'].apply(transform.classifica_turno)

# Salvando o DataFrame tratado em um novo arquivo CSV sem incluir o índice
df_work.to_csv("base_tratada.csv", index=False)