import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np

# MANIPULANDO O DATASET DE MINUTOS PARA MARCAR DOS JOGADORES DO BRASILEIRAO E COMPARANDO OS ATACANTES DO CRUZEIRO COM OS DEMAIS

# Lendo o dataset
data = pd.read_csv("../Datasets/Gols_per_min.csv")

# Calculando a media do Gilberto
gilberto = data[data["Jogador"] == "Gilberto"]
media_gil = gilberto["Tempo de Jogo"]/ gilberto["Gols"]
print(f"Media Gilberto: {int(media_gil.array[0])}")

# Calculando a media do Henrique Dourado
dourado = data[data["Jogador"] == "Henrique Dourado"]
media_dou = dourado["Tempo de Jogo"]/ dourado["Gols"]
print(f"Media Dourado: {int(media_dou.array[0])}")

# Filtrando o tempo de jogo para no minimo 330 minutos (Tempo de jogo do Henrique Dourado até a rodada 13)
min_tempo = data[data["Tempo de Jogo"] > 330]
min_tempo = min_tempo.reset_index(drop=True)

# Filtrando o dataset para um novo apenas com os atacantes do campeonato
df_atacantes = min_tempo[min_tempo["Posicao"] == "AT"]
df_atacantes = df_atacantes.reset_index(drop=True)

# Calculando as médias de cada atacante e descobrindo o melhor e o pior
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


# Visualizando as informações coletadas
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

# Separando as informações necessárias e plotando o gráfico
nome_melhor = df_atacantes.loc[i_melhor, "Jogador"]
nome_pior = df_atacantes.loc[i_pior, "Jogador"]

plotx = ["Henrique Dourado", "Gilberto", "Média dos Atacantes", nome_melhor, nome_pior]
ploty = [media_dou.array[0], media_gil.array[0], np.mean(medias), melhor, pior]

plt.figure(figsize=(10,8))
plot = plt.bar(plotx, ploty)
fonte = FontProperties(family='Arial', size=16)

for i, valor in enumerate(ploty):
    if i == 0 or i == 1:
        plot[i].set_color("blue")
    elif i == 2:
        plot[i].set_color("black")
    elif i == 3:
        plot[i].set_color("green")
    else:
        plot[i].set_color("red")

    plt.text(i, valor - 40, str(valor.round(2)), ha='center', color="white")

plt.title("Quanto tempo um atacante precisa para marcar no campeonato Brasileiro 2023?", color="white", pad=20, fontproperties=fonte)
plt.xlabel("Jogador", color="white", labelpad=15, fontproperties=fonte)
plt.ylabel("Tempo(Min)", color="white", labelpad=15, fontproperties=fonte)

plt.savefig("../Plots/gols_per_min_Gilberto_Dourado.png", transparent="True")
