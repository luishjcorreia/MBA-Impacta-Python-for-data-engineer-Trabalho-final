def calc_horas(df ,coluna_tempo_voo):

    # Divide os valores da coluna `coluna_minutos` por 60.
    df[coluna_tempo_voo] = df[coluna_tempo_voo] / 60
    # Retorna o dataframe `df` com a nova coluna `tempo_voo_horas`.

    coluna_transformada_hora = df

    return coluna_transformada_hora


def classifica_turno(coluna_data_hora):
    # Extrair a hora
    hora = coluna_data_hora.hour
    
    # Regra de classificação
    if 6 <= hora < 12:
        return 'MANHÃ'
    elif 12 <= hora < 18:
        return 'TARDE'
    elif 18 <= hora < 24:
        return 'NOITE'
    else:
        return 'MADRUGADA'