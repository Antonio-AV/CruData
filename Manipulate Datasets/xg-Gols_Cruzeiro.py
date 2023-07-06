import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# MANIPULANDO O DATASET DE XG-GOLS A DIIFERENÇA ENTRE ELES PARA CADA TIME DO BRASILEIRAO

# Lendo o dataset
data = pd.read_csv("../Datasets/xg-gols.csv")

# Calculando as dierenças
diferencas = []
for i in range(data.shape[0]):
    dif = data["Gols"][i] - data["xG"][i]
    diferencas.append(dif.round(2))

#Visualizando as informações coletadas
sorted_diferencas = np.sort(diferencas)
media = np.mean(diferencas)
print(diferencas)
print(media)
pior_dif = np.min(diferencas)
melhor_dif = np.max(diferencas)
s_pior_dif = sorted_diferencas[1]

pior_i = np.where(diferencas == pior_dif)
melhor_i = np.where(diferencas == melhor_dif)
s_pior_i = np.where(diferencas == s_pior_dif)

pior_time = data.loc[pior_i, "Time"]
melhor_time = data.loc[melhor_i, "Time"]
s_pior_time = data.loc[s_pior_i, "Time"]
print(melhor_time)
print(pior_time)
print(s_pior_time)


# Separando as informações necessárias e plotando o gráfico
times = data["Time"].array
times = np.array(times)
times = np.append(times, "Média")

diferencas.append(media)

plotx = times
ploty = diferencas

plot = plt.bar(plotx, ploty, facecolor="none")

plot[pior_i[0][0]].set_color('red')
plot[s_pior_i[0][0]].set_color('yellow')
plot[melhor_i[0][0]].set_color('green')
plot[-1].set_color('black')

for i, valor in enumerate(ploty):
    if i != pior_i[0][0] and i != s_pior_i[0][0] and i != melhor_i[0][0] and i != len(ploty)-1:
        plot[i].set_color("blue")
    if valor > 0:
        plt.text(i, valor + 0.05, str(valor.round(2)), ha='center', color="white")
    elif valor < 0:
        plt.text(i, valor - 0.40, str(valor.round(2)), ha='center', color="white")


plt.title("Gols - Expected Gols dos times do Brasileirão 2023", color="white", pad=15)
plt.xlabel("Time", color="white", labelpad=15)
plt.ylabel("Gols - xG", color="white", labelpad=15)

plt.savefig("../Plots/gols-xg.png", transparent="True")