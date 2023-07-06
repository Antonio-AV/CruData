import pandas as pd

# VISITA A PAGINA DE ESTATISTICAS DE CHUTES DO BRASILEIRAO E COMPARA A QUANTIDADE DE CHUTES NECESSÁRIAS PARA MARCAR

# Acessando a pagina de estatisticas do brasileirao
url = f"https://fbref.com/pt/comps/24/shooting/Serie-A-Estatisticas"
df = pd.read_html(url)[0]

# Separando os dados que interessam
times = df["Unnamed: 0_level_0"]
gols = df["Padrão", "Gols"]
chutes = df["Padrão", "TC"]

# Criando o novo dataframe e salvando-o
df_chutes_gols = pd.DataFrame({"Time": times["Equipe"],
                           "Gols": gols,
                           "Chutes":chutes})

df_chutes_gols.to_csv("../Datasets/Chutes_para_marcar_times.csv")


