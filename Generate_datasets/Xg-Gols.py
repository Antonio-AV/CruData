import pandas as pd
import json

# VISITA A PAGINA DE ESTATISTICAS DO BRASILEIRAO E COMPARA OS GOLS ESPERADOS(xG) E OS GOLS MARCADOS PARA CADA TIME DA COMPETIÇÃO

# Acessando a pagina de estatisticas do brasileirao
url = f"https://fbref.com/pt/comps/24/Serie-A-Estatisticas"
df = pd.read_html(url)[2]

# Separando os dados que interessam
times = df["Unnamed: 0_level_0"]
gols = df["Desempenho", "Gols"]
xg = df["Esperado", "xG"]

# Criando o novo dataframe e salvando-o
df_xg_gols = pd.DataFrame({"Time": times["Equipe"],
                           "Gols": gols,
                           "xG":xg})

df_xg_gols.to_csv("../Datasets/xg-gols.csv")