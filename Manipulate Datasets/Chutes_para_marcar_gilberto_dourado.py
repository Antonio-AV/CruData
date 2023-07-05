import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

data = pd.read_csv("../Datasets/Chutes_para_marcar.csv")


gilberto = data[data["Jogador"] == "Gilberto"]
media_gil = gilberto["Chutes"]/ gilberto["Gols"]
print(f"Chutes para marcar Gilberto: {media_gil.array[0].round(2)}")

dourado = data[data["Jogador"] == "Henrique Dourado"]
media_dou = dourado["Chutes"]/ dourado["Gols"]
print(f"Chuets para marcar Dourado: {media_dou.array[0].round(2)}")

df_atacantes = data[data["Posicao"] == "AT"]
df_atacantes = df_atacantes.reset_index(drop=True)

melhor = float('inf')
pior = 0
medias = []
for i in range(len(df_atacantes["Gols"])):
    media = df_atacantes["Chutes"][i]/ df_atacantes["Gols"][i]
    medias.append(media.round(2))

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
print(np.mean(medias).round(2))
pos_gilberto = np.where(medias == media_gil.array[0].round(2))
pos_dourado = np.where(medias == media_dou.array[0].round(2))
print(pos_dourado)
print(pos_gilberto)
print(len(medias))

nome_melhor = df_atacantes.loc[i_melhor, "Jogador"]
nome_pior = df_atacantes.loc[i_pior, "Jogador"]

plotx = ["Henrique Dourado", "Gilberto", "Média dos Atacantes", nome_melhor, nome_pior]
ploty = [media_dou.array[0], media_gil.array[0], np.mean(medias), melhor, pior]

plt.bar(plotx, ploty)

for i, valor in enumerate(ploty):
    plt.text(i, valor - 1.5, str(valor.round(2)), ha='center')

plt.title("Quantos chutes um atacante precisa para marcar no campeonato brasileiro?")
plt.xlabel("Jogador")
plt.ylabel("Chutes")

plt.show()
