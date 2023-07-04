import requests
import pandas as pd
import matplotlib.pyplot as plt
import json

test = open('times_brasileirao.json')
data = json.load(test)

gols_per_min = pd.DataFrame()

for i in range(len(data["Times"])):
    time = data["Times"][i]["Time"]
    id = data["Times"][i]["id"]

    url = f"https://fbref.com/pt/equipes/{id}/{time}-Estatisticas"
    df = pd.read_html(url)[0]

    nomes = []
    minutos = []
    gols = []
    for j in range(len(df["Unnamed: 0_level_0"])-2):
        jogador = df.loc[j, "Unnamed: 0_level_0"]
        nome = jogador.Jogador
        minuto = df["Tempo de jogo", "Min."][j]
        gol = df["Desempenho", "Gols"][j]
        nomes.append(nome)
        minutos.append(minuto)
        gols.append(gol)
    gols_per_min_time = pd.DataFrame({"Jogador": nomes,
                                      "Tempo de Jogo": minutos,
                                      "Gols": gols,
                                      "Time":time})
    gols_per_min_time = gols_per_min_time.dropna()
    gols_per_min_time = gols_per_min_time.drop(gols_per_min_time[gols_per_min_time["Gols"] == 0].index)
    print(gols_per_min_time)
    gols_per_min = pd.concat([gols_per_min, gols_per_min_time])

gols_per_min = gols_per_min.reset_index(drop=True)
print(gols_per_min)

for i in range(len(gols_per_min)):
    if gols_per_min["Tempo de Jogo"][i] < 2:
        gols_per_min["Tempo de Jogo"][i] = gols_per_min["Tempo de Jogo"][i] * 1000 

melhor = float('inf')
for i in range(len(gols_per_min)):
    media = gols_per_min["Tempo de Jogo"][i] / gols_per_min["Gols"][i]

    if media < melhor:
        melhor = media
        indice = i

print(melhor)
print(gols_per_min.loc[indice])

# print(df)


# gols = df["GP"]
# oponentes = df["Oponente"]

# plt.plot(oponentes, gols, marker="o", linestyle='-', color='b')

# plt.title("Gols X Adversários")
# plt.xlabel("Adversário")
# plt.ylabel("Gols")

# plt.xticks(rotation=45)

# plt.show()

