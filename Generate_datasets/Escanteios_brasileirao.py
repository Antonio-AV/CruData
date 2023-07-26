import pandas as pd

# ACESSANDO AS ESTATISTICAS DO BRASILEIRAO 2023 E PEGANDO OS TIPOS DE PASSE DOS TIMES

url = f"https://fbref.com/pt/comps/24/Serie-A-Estatisticas#all_stats_squads_passing_types"
df_nescanteios = pd.read_html(url)[12]

escanteios = []
times = []
gols = []

for j in range(len(df_nescanteios["Tipos de Passe"])):
        time = df_nescanteios.loc[j, "Unnamed: 0_level_0"].Equipe
        n_escanteios = df_nescanteios["Tipos de Passe", "CK"][j]

        times.append(time)
        escanteios.append(n_escanteios)


df_escanteios = pd.DataFrame({"Times": times,
                              "Escanteios": escanteios,})

df_escanteios.to_csv("../Datasets/Escanteios_brasileirao.csv")