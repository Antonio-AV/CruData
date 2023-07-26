import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# MANIPULANDO O DATASET DE ESCANTEIOS PARA DESCOBRIR A QTD DE ESCANTEIOS, DE GOLS DE ESCANTEIO, E APROVEITAMENTO DE CADA TIME DO BRASILEIRAO

# Lendo o dataset e descobrindo os piores/melhores
data = pd.read_csv("../Datasets/Escanteios_brasileirao.csv")

n_escanteios = data["Escanteios"].array
times = data["Times"].array

piores_i = np.argsort(n_escanteios)[:3]
melhores_i = np.argsort(n_escanteios)[::-1][:3]

piores_esc = n_escanteios[piores_i]
melhores_esc = n_escanteios[melhores_i]

piores_times = times[piores_i]
melhores_times = times[melhores_i]

print(melhores_times)
print(piores_times)


# Gols retirados de dados do ge e assistindo gols dos times (não encontrei fontes com os dados prontos) 
gols_america = 1
gols_athletico = 0
gols_atletico = 0
gols_bahia = 1
gols_botafogo = 3
gols_bragantino = 1
gols_corinthians = 2
gols_coritiba = 2
gols_cruzeiro = 2
gols_cuiaba = 3
gols_fla = 1
gols_flu = 4
gols_fortaleza = 2
gols_goias = 3
gols_gremio = 1
gols_inter = 4
gols_palmeiras = 4
gols_santos = 0
gols_sp = 2
gols_vasco = 0

gols = []

gols.append(gols_america)
gols.append(gols_athletico)
gols.append(gols_atletico)
gols.append(gols_bahia)
gols.append(gols_botafogo)
gols.append(gols_bragantino)
gols.append(gols_corinthians)
gols.append(gols_coritiba)
gols.append(gols_cruzeiro)
gols.append(gols_cuiaba)
gols.append(gols_fla)
gols.append(gols_flu)
gols.append(gols_fortaleza)
gols.append(gols_goias)
gols.append(gols_gremio)
gols.append(gols_inter)
gols.append(gols_palmeiras)
gols.append(gols_santos)
gols.append(gols_sp)
gols.append(gols_vasco)


# Gerando os aproveitamentos de cada time e analisando-os
aprovs = []
for i in range(len(times)):
    aprov = (gols[i] / n_escanteios[i])* 100
    aprovs.append(round(aprov, 2))

print(aprovs)
media = np.mean(aprovs)
pior_aprov = np.min(aprovs)
melhor_aprov = np.max(aprovs)

pior_i = np.where(aprovs == pior_aprov)
melhor_i = np.where(aprovs == melhor_aprov)

pior_time = times[pior_i]
melhor_time = times[melhor_i]

print(melhor_time)
print(pior_time)

times = np.array(times)
times = np.append(times, "Média")
aprovs.append(round(media,2))


# Gerando o Plot de aproveitamento
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
    plt.text(i, valor + 0.05, str(valor.round(2)), ha='center', color="white")



plt.title("Aproveitamento nos escanteios dos times do Brasileirão 2023", color="white", pad=15)
plt.xlabel("Time", color="white", labelpad=15)
plt.ylabel("Aproveitamento em %", color="white", labelpad=15)
plt.savefig("../Plots/Aproveitamento_ofensivo_cruzeiro_escanteios.png", transparent="True")

# Gerando o plot de numero de escanteios
media2 = np.mean(n_escanteios)
pior_escanteio = np.min(n_escanteios)
melhor_escanteio = np.max(n_escanteios)

pior_i2 = np.where(n_escanteios == pior_escanteio)
melhor_i2 = np.where(n_escanteios == melhor_escanteio)

pior_time2 = times[pior_i2]
melhor_time2 = times[melhor_i2]

print(melhor_time2)
print(pior_time2)

n_escanteios = np.array(n_escanteios)
n_escanteios = np.append(n_escanteios, round(media2,2))

plotx2 = times
ploty2 = n_escanteios

plt.figure(figsize=(10,8))
plot2 = plt.bar(plotx2, ploty2, facecolor="none")

plot2[pior_i2[0][0]].set_color('red')
plot2[melhor_i2[0][0]].set_color('green')
plot2[-1].set_color('black')

for i, valor in enumerate(ploty2):
    if i != pior_i2[0][0]  and i != melhor_i2[0][0] and i != len(ploty2)-1:
        plot2[i].set_color("white")
    plt.text(i, valor + 0.05, str(valor.round(2)), ha='center', color="white")



plt.title("Número de escanteios dos times do Brasileirão 2023", color="white", pad=15)
plt.xlabel("Time", color="white", labelpad=15)
plt.ylabel("Escanteios", color="white", labelpad=15)

plt.savefig("../Plots/Numero_de_escanteios.png", transparent="True")


# Gerando o plot de gols de escanteio
media3 = np.mean(gols)
pior_gols = np.min(gols)
melhor_gols = np.max(gols)

pior_i3 = np.where(gols == pior_gols)
melhor_i3 = np.where(gols == melhor_gols)

pior_time3 = times[pior_i3]
melhor_time3 = times[melhor_i3]

print(melhor_time3)
print(pior_time3)

gols.append(round(media3,2))
print(gols)
plotx3 = times
ploty3 = gols

plt.figure(figsize=(10,8))
plot3 = plt.bar(plotx3, ploty3, facecolor="none")
print(pior_i3[0])

for i, valor in enumerate(ploty3):
    if times[i] == "Cruzeiro":
        plot3[i].set_color("blue")
    else:
        plot3[i].set_color("white")
    if type(valor) != int:
        plt.text(i, valor + 0.05, str(valor.round(2)), ha='center', color="white")
    else:
        plt.text(i, valor + 0.05, str(valor), ha='center', color="white")

for i in range(len(melhor_i3[0])):
    plot3[melhor_i3[0][i]].set_color('green')

plot3[pior_i3[0][0]].set_color('red')
plot3[-1].set_color('black')


plt.title("Número de gols de escanteios dos times do Brasileirão 2023", color="white", pad=15)
plt.xlabel("Time", color="white", labelpad=15)
plt.ylabel("Gols", color="white", labelpad=15)

plt.savefig("../Plots/Numero_de_gols_de_escanteios.png", transparent="True")








