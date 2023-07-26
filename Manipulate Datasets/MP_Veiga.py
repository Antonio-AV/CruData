import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json
import os

# ORganizando Plot 1 com as características gerais

data = pd.read_csv("../Datasets/MP_Veiga.csv")

jogos = data["Jogos"]
gols = data["Gols"]
assists = data["Assistencias"]
participacoes = data["Participações em Gols"]

aspectos = ['Jogos', 'Gols', 'Assistências', 'Participações']

# Valores para cada jogador em cada aspecto (dados de exemplo)
valores_jogador1 = [-1 * jogos[0], -1 * gols[0], -1 * assists[0], -1 * participacoes[0]]
valores_jogador2 = [jogos[1], gols[1], assists[1], participacoes[1]]

# Criando o gráfico de barras horizontais
plt.figure(figsize=(10, 8))

# Coordenadas dos eixos y para posicionar as barras horizontalmente
y_pos = range(len(aspectos))

# Plotando as barras para o Jogador 1
plt.barh(y_pos, valores_jogador1, height=0.4, color='blue', label='Matheus Pereira', align='center')

# Plotando as barras para o Jogador 2
plt.barh(y_pos, valores_jogador2, height=0.4, color='green', label='Raphael Veiga', align='center')

for i, valor in enumerate(valores_jogador1):
    plt.text(valor - 0.5, i, str(valor*-1), color='black', ha='right', va='center', fontweight='bold')

for i, valor in enumerate(valores_jogador2):
    plt.text(valor + 0.5, i,  str(valor), color='black', ha='left', va='center', fontweight='bold')

# Configurando os rótulos do eixo y com os aspectos
plt.yticks(y_pos, aspectos)

# Configurando o eixo x
plt.xlabel('Valores')
plt.axvline(x=0, color='black', linewidth=0.8)  # Linha vertical no centro

# Adicionando título do gráfico
plt.title('Comparação de Números entre Matheus Pereira (2020-2021) e Raphael Veiga (2021)')

plt.savefig("../Plots/MP_Veiga/dados_gerais.png", transparent="True")

#####################################################################################################################

# Organizando o plot 2 com os dados de finalizações

chutes = data["Chutes"]
chutes_para_marcar = data["Chutes para Marcar"]

aspectos = ['Chutes', 'Chutes p/ Marcar']

# Valores para cada jogador em cada aspecto (dados de exemplo)
valores_jogador1 = [-1 * chutes[0], -1 * chutes_para_marcar[0]]
valores_jogador2 = [chutes[1], chutes_para_marcar[1]]

# Criando o gráfico de barras horizontais
plt.figure(figsize=(10, 8))

# Coordenadas dos eixos y para posicionar as barras horizontalmente
y_pos = range(len(aspectos))

# Plotando as barras para o Jogador 1
plt.barh(y_pos, valores_jogador1, height=0.4, color='blue', label='Matheus Pereira', align='center')

# Plotando as barras para o Jogador 2
plt.barh(y_pos, valores_jogador2, height=0.4, color='green', label='Raphael Veiga', align='center')

for i, valor in enumerate(valores_jogador1):
    plt.text(valor - 0.5, i, str(valor*-1), color='black', ha='right', va='center', fontweight='bold')

for i, valor in enumerate(valores_jogador2):
    plt.text(valor + 0.5, i,  str(valor), color='black', ha='left', va='center', fontweight='bold')

# Configurando os rótulos do eixo y com os aspectos
plt.yticks(y_pos, aspectos, fontweight="bold")

# Configurando o eixo x
plt.xlabel('Valores', fontweight="bold")
plt.axvline(x=0, color='black', linewidth=0.8)  # Linha vertical no centro

# Adicionando título do gráfico
plt.title('Comparação de Finalizações entre Matheus Pereira (2020-2021) e Raphael Veiga (2021)')

plt.savefig("../Plots/MP_Veiga/finalizacoes.png", transparent="True")

#####################################################################################################################

# Organizando o plot 3 com os tipos de passes

passes = data["Passes"]
passes_progressivos = data["Passes progressivos"]
passes_para_chutes = data["Passes para chutes"]

aspectos = ['Passes', 'Progressivos', "Passes p/ chutes"]

# Valores para cada jogador em cada aspecto (dados de exemplo)
valores_jogador1 = [-1 * passes[0], -1 * passes_progressivos[0], -1 * passes_para_chutes[0]]
valores_jogador2 = [passes[1], passes_progressivos[1], passes_para_chutes[1]]

# Criando o gráfico de barras horizontais
plt.figure(figsize=(10, 8))

# Coordenadas dos eixos y para posicionar as barras horizontalmente
y_pos = range(len(aspectos))

# Plotando as barras para o Jogador 1
plt.barh(y_pos, valores_jogador1, height=0.4, color='blue', label='Matheus Pereira', align='center')

# Plotando as barras para o Jogador 2
plt.barh(y_pos, valores_jogador2, height=0.4, color='green', label='Raphael Veiga', align='center')

for i, valor in enumerate(valores_jogador1):
    plt.text(valor - 0.5, i, str(valor*-1), color='black', ha='right', va='center', fontweight='bold')

for i, valor in enumerate(valores_jogador2):
    plt.text(valor + 0.5, i,  str(valor), color='black', ha='left', va='center', fontweight='bold')

# Configurando os rótulos do eixo y com os aspectos
plt.yticks(y_pos, aspectos)

# Configurando o eixo x
plt.xlabel('Valores')
plt.axvline(x=0, color='black', linewidth=0.8)  # Linha vertical no centro

# Adicionando título do gráfico
plt.title('Comparação de Passes entre Matheus Pereira (2020-2021) e Raphael Veiga (2021)')

plt.savefig("../Plots/MP_Veiga/tipos_de_passes.png", transparent="True")

#####################################################################################################################

# Organizando o plot 4 com os aproveitamentos de passes e dribles

aprov_passes = data["Aproveitamento de passes"]
aprov_passes_curtos = data["Aproveitamento de passes curtos"]
aprov_passes_medios = data["Aproveitamento de passes medios"]
aprov_passes_longos = data["Aproveitamento de passes longos"]
aprov_dribles = data["Aproveitamento de dribles"]

aspectos = ['Passes', 'Passes curtos', "Passes medios", "Passes longos", "Dribles"]

# Valores para cada jogador em cada aspecto (dados de exemplo)
valores_jogador1 = [-1 * aprov_passes[0], -1 * aprov_passes_curtos[0], -1 * aprov_passes_medios[0], -1 * aprov_passes_longos[0], -1 * aprov_dribles[0]]
valores_jogador2 = [aprov_passes[1], aprov_passes_curtos[1], aprov_passes_medios[1], aprov_passes_longos[1], aprov_dribles[1]]

# Criando o gráfico de barras horizontais
plt.figure(figsize=(10, 8))

# Coordenadas dos eixos y para posicionar as barras horizontalmente
y_pos = range(len(aspectos))

# Plotando as barras para o Jogador 1
plt.barh(y_pos, valores_jogador1, height=0.4, color='blue', label='Matheus Pereira', align='center')

# Plotando as barras para o Jogador 2
plt.barh(y_pos, valores_jogador2, height=0.4, color='green', label='Raphael Veiga', align='center')

for i, valor in enumerate(valores_jogador1):
    plt.text(valor - 0.5, i, str(valor*-1), color='black', ha='right', va='center', fontweight='bold')

for i, valor in enumerate(valores_jogador2):
    plt.text(valor + 0.5, i,  str(valor), color='black', ha='left', va='center', fontweight='bold')

# Configurando os rótulos do eixo y com os aspectos
plt.yticks(y_pos, aspectos)

# Configurando o eixo x
plt.xlabel('Valores em %')
plt.axvline(x=0, color='black', linewidth=0.8)  # Linha vertical no centro

# Adicionando título do gráfico
plt.title('Aproveitamento de passes e dribles de Matheus Pereira (2020-2021) e Raphael Veiga (2021)')

plt.savefig("../Plots/MP_Veiga/aprovs_passes_dribles.png", transparent="True")

#####################################################################################################################

# Organizando o plot 5 com os toques na bola

toques = data["Toques na bola"]
toques_defesa = data["Toques na defesa"]
toques_meio = data["Toques no meio"]
toques_ataque = data["Toques na ataque"]

aspectos = ['Total', 'Defesa', "Meio", "Ataque"]

# Valores para cada jogador em cada aspecto (dados de exemplo)
valores_jogador1 = [-1 * toques[0], -1 * toques_defesa[0], -1 * toques_meio[0], -1 * toques_ataque[0]]
valores_jogador2 = [toques[1], toques_defesa[1], toques_meio[1], toques_ataque[1]]

# Criando o gráfico de barras horizontais
plt.figure(figsize=(10, 8))

# Coordenadas dos eixos y para posicionar as barras horizontalmente
y_pos = range(len(aspectos))

# Plotando as barras para o Jogador 1
plt.barh(y_pos, valores_jogador1, height=0.4, color='blue', label='Matheus Pereira', align='center')

# Plotando as barras para o Jogador 2
plt.barh(y_pos, valores_jogador2, height=0.4, color='green', label='Raphael Veiga', align='center')

for i, valor in enumerate(valores_jogador1):
    if i == 0:
        plt.text(valor + 0.5, i,  str(valor*-1), color='black', ha='left', va='center', fontweight='bold')
    else:
        plt.text(valor - 0.5, i, str(valor*-1), color='black', ha='right', va='center', fontweight='bold')

for i, valor in enumerate(valores_jogador2):
    if i == 0:
        plt.text(valor + 0.5, i,  str(valor), color='black', ha='left', va='center', fontweight='bold')
    else:
        plt.text(valor + 0.5, i,  str(valor), color='black', ha='left', va='center', fontweight='bold')

# Configurando os rótulos do eixo y com os aspectos
plt.yticks(y_pos, aspectos)

# Configurando o eixo x
plt.xlabel('Valores')
plt.axvline(x=0, color='black', linewidth=0.8)  # Linha vertical no centro

# Adicionando título do gráfico
plt.title('Comparando os toques na bola de Matheus Pereira (2020-2021) e Raphael Veiga (2021)')

plt.savefig("../Plots/MP_Veiga/toques_na_bola.png", transparent="True")