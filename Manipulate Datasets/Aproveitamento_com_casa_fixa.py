import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import os

# MANIPULANDO O DATASET DE JOGOS DE CADA TIME DO BRASILEIRÃO E COMPARANDO O DESEMPENHO EM CASA DE TIMES COM CASA FIXA E NAO FIXA


# Lendo o dataset
prefix = "../Datasets/Jogos_times_serieA/"

# Filtrando apenas para jogos de mandantes
df_casa = pd.DataFrame()

for time in os.listdir(prefix):
    data = pd.read_csv(prefix+time)
    data["Time"] = time[:-4]
    for i in range(data.shape[0]):
        data = data.drop(data[data["Local"] == "Visitante"].index)
    df_casa = pd.concat([df_casa, data])
    
df_casa = df_casa.reset_index(drop=True)
df_casa.to_csv("../Datasets/Jogos_como_mandantes.csv")

# Separando os estadios de cada mandante à cada jogo
info = open('../times_brasileirao.json')
times = json.load(info)

casas_america = []
casas_athletico = []
casas_atletico = []
casas_bahia = []
casas_botafogo = []
casas_bragantino = []
casas_corinthians = []
casas_coritiba = []
casas_cruzeiro = []
casas_cuiaba = []
casas_flamengo = []
casas_fluminense = []
casas_fortaleza = []
casas_goias = []
casas_gremio = []
casas_internacional = []
casas_palmeiras = []
casas_santos = []
casas_sp = []
casas_vasco = []

for i in range(len(times["Times"])):
    time = times["Times"][i]["Time"]
    for j in range(df_casa.shape[0]):
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "America-MG":
            if df_casa["Estádio"][j] not in casas_america:
                casas_america.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Atletico-Paranaense":
            if df_casa["Estádio"][j] not in casas_athletico:
                casas_athletico.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Atletico-Mineiro":
            if df_casa["Estádio"][j] not in casas_atletico:
                casas_atletico.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Bahia":
            if df_casa["Estádio"][j] not in casas_bahia:
                casas_bahia.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Botafogo-RJ":
            if df_casa["Estádio"][j] not in casas_botafogo:
                casas_botafogo.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Bragantino":
            if df_casa["Estádio"][j] not in casas_bragantino:
                casas_bragantino.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Corinthians":
            if df_casa["Estádio"][j] not in casas_corinthians:
                casas_corinthians.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Coritiba":
            if df_casa["Estádio"][j] not in casas_coritiba:
                casas_coritiba.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Cruzeiro":
            if df_casa["Estádio"][j] not in casas_cruzeiro:
                casas_cruzeiro.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Cuiaba":
            if df_casa["Estádio"][j] not in casas_cuiaba:
                casas_cuiaba.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Flamengo":
            if df_casa["Estádio"][j] not in casas_flamengo:
                casas_flamengo.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Fluminense":
            if df_casa["Estádio"][j] not in casas_fluminense:
                casas_fluminense.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Fortaleza":
            if df_casa["Estádio"][j] not in casas_fortaleza:
                casas_fortaleza.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Goias":
            if df_casa["Estádio"][j] not in casas_goias:
                casas_goias.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Gremio":
            if df_casa["Estádio"][j] not in casas_gremio:
                casas_gremio.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Internacional":
            if df_casa["Estádio"][j] not in casas_internacional:
                casas_internacional.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Palmeiras":
            if df_casa["Estádio"][j] not in casas_palmeiras:
                casas_palmeiras.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Santos":
            if df_casa["Estádio"][j] not in casas_santos:
                casas_santos.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Sao-Paulo":
            if df_casa["Estádio"][j] not in casas_sp:
                casas_sp.append(df_casa["Estádio"][j])
        if time == df_casa["Time"][j] and df_casa["Time"][j] == "Vasco-da-Gama":
            if df_casa["Estádio"][j] not in casas_vasco:
                casas_vasco.append(df_casa["Estádio"][j])

todas_casas = []

todas_casas.append(casas_america)
todas_casas.append(casas_athletico)
todas_casas.append(casas_atletico)
todas_casas.append(casas_bahia)
todas_casas.append(casas_botafogo)
todas_casas.append(casas_bragantino)
todas_casas.append(casas_corinthians)
todas_casas.append(casas_coritiba)
todas_casas.append(casas_cruzeiro)
todas_casas.append(casas_cuiaba)
todas_casas.append(casas_flamengo)
todas_casas.append(casas_fluminense)
todas_casas.append(casas_fortaleza)
todas_casas.append(casas_goias)
todas_casas.append(casas_gremio)
todas_casas.append(casas_internacional)
todas_casas.append(casas_palmeiras)
todas_casas.append(casas_santos)
todas_casas.append(casas_sp)
todas_casas.append(casas_vasco)

print(todas_casas)


# Separando os mandante em fixos e nomades
nomades_index = []
for i in range(len(todas_casas)):
    if len(todas_casas[i]) > 1:
        nomades_index.append(i)

print(nomades_index)

nomade_aprovs = []
fixos_aprovs = []
for i in range(len(times["Times"])):
    time = times["Times"][i]["Time"]
    pontos = 0
    cont_nomades = 0
    cont_fixos = 0
    for j in range(df_casa.shape[0]):
        if i in nomades_index and df_casa["Time"][j] == time:
            cont_nomades += 1
            if df_casa["Resultado"][j] == "V":
                pontos += 3
            elif df_casa["Resultado"][j] == "E":
                pontos += 1
        elif i not in nomades_index and df_casa["Time"][j] == time:
            cont_fixos += 1
            if df_casa["Resultado"][j] == "V":
                pontos += 3
            elif df_casa["Resultado"][j] == "E":
                pontos += 1
    if cont_nomades > 0:
        aprov = (pontos/(cont_nomades * 3))*100
        nomade_aprovs.append(round(aprov,2))
    elif cont_fixos > 0:
        aprov = (pontos/(cont_fixos * 3))*100
        fixos_aprovs.append(round(aprov, 2))

# Visualizando os resultados e preparando-os para plotar
print(nomade_aprovs)
print(fixos_aprovs)

media_nomades = round(np.mean(nomade_aprovs),2)
media_fixos = round(np.mean(fixos_aprovs),2)

times_nomades = []

for i in nomades_index:
    times_nomades.append(times["Times"][i]["Time"])

times_nomades.append("Média Casa Variada")
times_nomades.append("Média Casa Fixa")
nomade_aprovs.append(media_nomades)
fixos_aprovs.append(media_fixos)

print(times_nomades)

#Fazendo o plot
plotx = times_nomades
ploty = nomade_aprovs
ploty.append(fixos_aprovs[-1])
print(ploty)

pior_aprov = np.min(nomade_aprovs)
melhor_aprov = np.max(nomade_aprovs)

pior_i = np.where(ploty == pior_aprov)
melhor_i = np.where(ploty == melhor_aprov)

pior_i = pior_i[0][0]
melhor_i = melhor_i[0][0]

plt.figure(figsize=(10,8))
plot = plt.bar(plotx, ploty, facecolor="none")

plot[pior_i].set_color('red')
plot[melhor_i].set_color('green')

for i, valor in enumerate(ploty):
    if plotx[i] == "Cruzeiro":
        plot[i].set_color("blue")
    elif i != pior_i  and i != melhor_i:
        plot[i].set_color("white")
    plt.text(i, valor + 0.5, str(valor), ha='center', color="white")
    


plt.title("Aproveitamento dos mandantes 'nômades' do Brasileirão 2023", color="white", pad=15)
plt.xlabel("Time", color="white", labelpad=15)
plt.ylabel("Aproveitamento em %", color="white", labelpad=15)

plt.savefig("../Plots/Aproveitamento_Mandantes_Nomades.png", transparent="True")




