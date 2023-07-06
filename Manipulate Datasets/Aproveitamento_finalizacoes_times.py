import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# MANIPULANDO O DATASET DE XG-GOLS A DIIFERENÇA ENTRE ELES PARA CADA TIME DO BRASILEIRAO

# Lendo o dataset
data = pd.read_csv("../Datasets/Chutes_para_marcar_times.csv")

# Calculando os aproveitamentos
aprovs = []
for i in range(data.shape[0]):
    aprov = (data["Gols"][i] / data["Chutes"][i]) * 100
    aprovs.append(aprov.round(2))

#Visualizando as informações coletadas
sorted_aprovs = np.sort(aprovs)
media = np.mean(aprovs)
print(aprovs)
print(media)
pior_aprov = np.min(aprovs)
melhor_aprov = np.max(aprovs)

pior_i = np.where(aprovs == pior_aprov)
melhor_i = np.where(aprovs == melhor_aprov)

pior_time = data.loc[pior_i, "Time"]
melhor_time = data.loc[melhor_i, "Time"]

print(melhor_time)
print(pior_time)


# Separando as informações necessárias e plotando o gráfico
times = data["Time"].array
times = np.array(times)
times = np.append(times, "Média")

aprovs.append(media)

plotx = times
ploty = aprovs

plt.figure(figsize=(10,8))
plot = plt.bar(plotx, ploty, facecolor="none")

plot[pior_i[0][0]].set_color('red')
plot[melhor_i[0][0]].set_color('green')
plot[-1].set_color('black')

for i, valor in enumerate(ploty):
    if times[i] == "Cruzeiro":
        plot[i].set_color("blue")
    elif i != pior_i[0][0]  and i != melhor_i[0][0] and i != len(ploty)-1:
        plot[i].set_color("white")
    if valor > 0:
        plt.text(i, valor + 0.05, str(valor.round(2)), ha='center', color="white")
    elif valor < 0:
        plt.text(i, valor - 0.40, str(valor.round(2)), ha='center', color="white")


plt.title("Aproveitamento das finalizações dos times do Brasileirão 2023", color="white", pad=15)
plt.xlabel("Time", color="white", labelpad=15)
plt.ylabel("Aproveitamento em %", color="white", labelpad=15)

plt.savefig("../Plots/Aproveitamento_finalizacoes_times.png", transparent="True")


