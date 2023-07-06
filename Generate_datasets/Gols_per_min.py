import pandas as pd
import json

# VISITA AS PAGINAS INICIAIS DE ESTATISTICAS DE CADA TIME BRASILEIRO E FILTRA AS INFORMAÇÕES DO NOME DO JOGADOR, CHUTES, GOLS E POSIÇÃO

# Percorrendo os times do brasileirao
test = open('../times_brasileirao.json')
data = json.load(test)

df_gols_per_min = pd.DataFrame()

for i in range(len(data["Times"])):
    time = data["Times"][i]["Time"]
    id = data["Times"][i]["id"]

    url = f"https://fbref.com/pt/equipes/{id}/{time}-Estatisticas"
    df = pd.read_html(url)[0]

    # Separando as informações que me interessam e formando um novo dataframe
    nomes = []
    minutos = []
    gols = []
    posicoes = []
    for j in range(len(df["Unnamed: 0_level_0"])-2):
        jogador = df.loc[j, "Unnamed: 0_level_0"]
        nome = jogador.Jogador
        minuto = df["Tempo de jogo", "Min."][j]
        gol = df["Desempenho", "Gols"][j]
        posicao = df["Unnamed: 2_level_0", "Pos."][j]
        nomes.append(nome)
        minutos.append(minuto)
        gols.append(gol)
        posicoes.append(posicao)
    df_gols_per_min_time = pd.DataFrame({"Jogador": nomes,
                                      "Tempo de Jogo": minutos,
                                      "Gols": gols,
                                      "Time":time,
                                      "Posicao":posicoes})
    # Filtrando os dados do novo dataframe
    df_gols_per_min_time = df_gols_per_min_time.dropna()
    df_gols_per_min_time = df_gols_per_min_time.drop(df_gols_per_min_time[df_gols_per_min_time["Gols"] == 0].index)
    
    # Concatenando os dataframes de cada time em um dataframe com todos os times
    df_gols_per_min = pd.concat([df_gols_per_min, df_gols_per_min_time])


# Ajustando o dataframe final e salvando-o
df_gols_per_min = df_gols_per_min.reset_index(drop=True)
for i in range(len(df_gols_per_min)):
    if df_gols_per_min["Tempo de Jogo"][i] < 2:
        df_gols_per_min["Tempo de Jogo"][i] = df_gols_per_min["Tempo de Jogo"][i] * 1000

df_gols_per_min.to_csv("../Datasets/Gols_per_min.csv") 