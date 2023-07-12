import pandas as pd
import json
# COMO NÃO TEM COMO VERIFICAR ESSES DADOS ATRAVES DE CÓDIGO PELO FOOTBALL REFERENCE, FAREI A PLANILHA MANUALMENTE SOBRE O APROVEITAMENTO EM CASA 
# DAS EQUIPES DO BRASILEIRAO 2023

# Percorrendo os times do brasileirao
test = open('../times_brasileirao.json')
data = json.load(test)


# Filtrando apenas as partidas do Brasileirao 23
for i in range(len(data["Times"])):
    time = data["Times"][i]["Time"]
    id = data["Times"][i]["id"]

    url = f"https://fbref.com/pt/equipes/{id}/{time}-Estatisticas"
    df_time = pd.read_html(url)[1]
    for j in range(df_time.shape[0]):
        df_time = df_time.drop(df_time[df_time["Relatório da Partida"] == "Confronto"].index)
        df_time = df_time.drop(df_time[df_time["Camp."] == "Sudamericana"].index)
        df_time = df_time.drop(df_time[df_time["Camp."] == "Libertadores"].index)
    print(df_time)
    df_time.to_csv(f"../Datasets/Jogos_times_serieA/{time}.csv")

