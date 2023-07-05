import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("../Datasets/Gols_per_min.csv")


gilberto = data[data["Jogador"] == "Gilberto"]
media_gil = gilberto["Tempo de Jogo"]/ gilberto["Gols"]
print(f"Media Gilberto: {int(media_gil.array[0])}")

dourado = data[data["Jogador"] == "Henrique Dourado"]
media_dou = dourado["Tempo de Jogo"]/ dourado["Gols"]
print(f"Media Dourado: {int(media_dou.array[0])}")

min_tempo = data[data["Tempo de Jogo"] > 330]
min_tempo = min_tempo.reset_index(drop=True)

df_atacantes = min_tempo[min_tempo["Posicao"] == "AT"]
df_atacantes = df_atacantes.reset_index(drop=True)

melhor = float('inf')
pior = 0
medias = []
for i in range(len(df_atacantes["Gols"])):
    media = df_atacantes["Tempo de Jogo"][i]/ df_atacantes["Gols"][i]
    medias.append(int(media))

    if media < melhor:
        melhor = media
        i_melhor = i

    if media > pior:
        pior = media
        i_pior = i


medias = np.array(medias)
medias = np.sort(medias)
print(melhor)
print(df_atacantes.loc[i_melhor])
print(pior)
print(df_atacantes.loc[i_pior])
print(medias)
print(np.mean(medias))
pos_gilberto = np.where(medias == media_gil.array[0])
pos_dourado = np.where(medias == media_dou.array[0])
print(pos_dourado)
print(pos_gilberto)
print(len(medias))

nome_melhor = df_atacantes.loc[i_melhor, "Jogador"]
nome_pior = df_atacantes.loc[i_pior, "Jogador"]

plotx = ["Henrique Dourado", "Gilberto", "Média dos Atacantes", nome_melhor, nome_pior]
ploty = [media_dou.array[0], media_gil.array[0], np.mean(medias), melhor, pior]

plt.bar(plotx, ploty)

for i, valor in enumerate(ploty):
    plt.text(i, valor - 40, str(valor.round(2)), ha='center')

plt.title("Quanto tempo um atacante precisa para marcar no campeonato Brasileiro?")
plt.xlabel("Jogador")
plt.ylabel("Tempo(Min)")

plt.show()
