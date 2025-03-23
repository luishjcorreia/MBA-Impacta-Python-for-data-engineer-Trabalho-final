import pandas as pd
import datetime
import numpy as np
import re

# Definição das colunas a serem utilizadas no DataFrame
usecols = ["year", "month", "day", "hour", "minute", "arr_delay", "carrier", "flight", "air_time", "distance", "origin", "dest"]

# Função para padronizar strings, removendo caracteres especiais e convertendo para maiúsculas
def padroniza_str(obs):
    return re.sub('[^A-Za-z0-9]+', '', obs.upper())

# Função para limpar e transformar o DataFrame
def retira_vazio(df):
    # Filtrando o DataFrame para remover linhas com valores ausentes nas colunas essenciais
    df_raw = df.loc[
        (~df["carrier"].isna()) &
        (~df["flight"].isna()) &
        (~df["year"].isna()) &
        (~df["hour"].isna()) &
        (~df["minute"].isna()) &
        (~df["month"].isna()) &
        (~df["day"].isna()) &
        (df["air_time"] > 0)  # Garante que o tempo de voo seja maior que zero
    ].loc[:, usecols]
    
    # Removendo duplicatas
    df_raw.drop_duplicates(inplace=True)
    
    # Criando uma cópia temporária do DataFrame para novo processamento
    tmp = df.loc[:, usecols].copy()
    tmp = tmp[tmp["air_time"] > 0]
    
    # Iterando sobre as colunas essenciais para remover valores nulos
    for col in ["carrier", "flight", "year", "month", "day", "hour", "minute"]:
        tmp_df = tmp.loc[~df[col].isna()]
        tmp = tmp_df.copy()
    
    # Criando uma nova coluna de data e hora combinando as colunas individuais
    df_raw["date_time"] = pd.to_datetime(df_raw[["year", "month", "day", "hour", "minute"]], dayfirst=True)
    
    # Definição das colunas finais do DataFrame
    usecols2 = ["date_time", "arr_delay", "carrier", "flight", "air_time", "distance", "origin", "dest"]
    new_columns = ["data_hora", "atraso_chegada", "companhia", "id_voo", "tempo_voo", "distancia", "origem", "destino"]
    
    # Criando um dicionário de mapeamento para renomear as colunas
    columns_map = {usecols2[i]: new_columns[i] for i in range(len(usecols2))}
    
    # Criando um novo DataFrame somente com as colunas necessárias e renomeando-as
    df_work = df_raw.loc[:, usecols2].copy()
    df_work.rename(columns=columns_map, inplace=True)
    
    # Convertendo os tipos de dados de algumas colunas para garantir consistência
    df_work["distancia"] = df_work["distancia"].astype(float)
    df_work["companhia"] = df_work["companhia"].astype(str)
    df_work["id_voo"] = df_work["id_voo"].astype(str)
    df_work["atraso_chegada"] = df_work["atraso_chegada"].astype(str)
    df_work["origem"] = df_work["origem"].astype(str)
    df_work["destino"] = df_work["destino"].astype(str)
    
    # Aplicando a função de padronização de string nas colunas categóricas
    df_work["companhia"] = df_work["companhia"].apply(lambda x: padroniza_str(x))
    df_work["id_voo"] = df_work["id_voo"].apply(lambda x: padroniza_str(x))
    df_work["origem"] = df_work["origem"].apply(lambda x: padroniza_str(x))
    df_work["destino"] = df_work["destino"].apply(lambda x: padroniza_str(x))
    
    return df_work
