import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# MANIPULANDO O DATASET DE MANDANTE DO CRUZEIRO E VERIFICANDO SEU DESEMPENHO EM CADA ESTADIO

# Lendo o dataset
data = pd.read_csv("../Datasets/Jogos_como_mandantes.csv")

# Separando as informações do Cruzeiro
cruzeiro_info = data[data["Time"] == "Cruzeiro"]
print(cruzeiro_info)

estadios = cruzeiro_info["Estádio"].array
resultados = cruzeiro_info["Resultado"].array
gols = cruzeiro_info["GP"].array

# Apurando os dados de cada estadio
est_aprov = np.unique(estadios)
print(estadios)

cont_indepa = 0
pontos_indepa = 0

cont_mineirao = 0
pontos_mineirao = 0

cont_jacare = 0
pontos_jacare = 0

cont_sabia = 0
pontos_sabia = 0


for i in range(len(estadios)):
    if estadios[i] == est_aprov[0]:
        cont_jacare += 1
        if resultados[i] == "V":
            pontos_jacare += 3
        elif resultados[i] == "E":
            pontos_jacare += 1
    if estadios[i] == est_aprov[1]:
        cont_indepa += 1
        if resultados[i] == "V":
            pontos_indepa += 3
        elif resultados[i] == "E":
            pontos_indepa += 1
    if estadios[i] == est_aprov[2]:
        cont_mineirao += 1
        if resultados[i] == "V":
            pontos_mineirao += 3
        elif resultados[i] == "E":
            pontos_mineirao += 1
    if estadios[i] == est_aprov[3]:
        cont_sabia += 1
        if resultados[i] == "V":
            pontos_sabia += 3
        elif resultados[i] == "E":
            pontos_sabia += 1

aprovs = []

aprov_jacare = (pontos_jacare/(cont_jacare * 3) * 100)
aprov_indepa = (pontos_indepa/(cont_indepa * 3) * 100)
aprov_mineirao = (pontos_mineirao/(cont_mineirao * 3) * 100)
aprov_sabia = (pontos_sabia/(cont_sabia * 3) * 100)

aprovs.append(aprov_jacare)
aprovs.append(aprov_indepa)
aprovs.append(aprov_mineirao)
aprovs.append(aprov_sabia)

print(aprovs)

plotx = est_aprov
ploty = aprovs

# Plotando as informações
plt.figure(figsize=(10,8))
plot = plt.bar(plotx, ploty, facecolor="none")


for i, valor in enumerate(ploty):
    plot[i].set_color("blue")
    plt.text(i, valor + 0.5, str(valor), ha='center', color="white")
    

plt.title("Aproveitamento do Cruzeiro em cada 'casa' no Brasileirão 2023", color="white", pad=15)
plt.xlabel("Estádio", color="white", labelpad=15)
plt.ylabel("Aproveitamento em %", color="white", labelpad=15)

plt.savefig("../Plots/Aproveitamento_Cruzeiro_cada_casa.png", transparent="True")
