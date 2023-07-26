import numpy as np
import pandas as pd

url = f"https://fbref.com/pt/stathead/player_comparison.cgi?request=1&sum=0&player_id1=b04ee927&p1yrfrom=2020-2021&player_id2=6e5a3bc7&p2yrfrom=2021"

df = pd.read_html(url)
print(df[0])

df_basic = df[0]
jogos = []
gols = []
assists = []
participacoes = []
for i in range(df_basic.shape[0]):
    n_jogos = df_basic.loc[i]["Tempo de jogo", "MP"]
    jogos.append(n_jogos)

    n_gols = df_basic.loc[i]["Desempenho", "Gols"]
    gols.append(n_gols)

    n_assists = df_basic.loc[i]["Desempenho", "Assis."]
    assists.append(n_assists)

    n_participacoes = df_basic.loc[i]["Desempenho", "G+A"]
    participacoes.append(n_participacoes)


df_chutes = df[1]
chutes = []
chutes_para_marcar = []
for i in range(df_chutes.shape[0]):
    n_chutes = df_chutes.loc[i]["Padrão", "TC"]
    n_chutes_para_marcar = n_chutes/gols[i]

    chutes.append(n_chutes)
    chutes_para_marcar.append(round(n_chutes_para_marcar,2))


df_passes = df[2]
passes = []
aprovs_passes = []
aprovs_curto = []
aprovs_medio = []
aprovs_longo = []
passes_progressivos = []
passes_chute = []
for i in range(df_passes.shape[0]):
    n_passes = df_passes.loc[i]["Total", "Cmp"]
    aprov_passes = df_passes.loc[i]["Total", "Cmp%"]/10
    aprov_curto = df_passes.loc[i]["Curto", "Cmp%"]/10
    aprov_medio = df_passes.loc[i]["Médio", "Cmp%"]/10
    aprov_longo = df_passes.loc[i]["Longo", "Cmp%"]/10
    passe_progressivo = df_passes.loc[i]["Unnamed: 28_level_0", "PrgP"]
    passe_chute = df_passes.loc[i]["Unnamed: 24_level_0", "KP"]

    passes.append(n_passes)
    aprovs_passes.append(aprov_passes)
    aprovs_curto.append(aprov_curto)
    aprovs_medio.append(aprov_medio)
    aprovs_longo.append(aprov_longo)
    passes_progressivos.append(passe_progressivo)
    passes_chute.append(passe_chute)

print(aprovs_passes)

df_posse = df[6]
toques = []
toques_def = []
toques_meio = []
toques_ataque = []
aprovs_dribles = []
for i in range(df_posse.shape[0]):
    toque = df_posse.loc[i]["Contatos", "Contatos"]
    toque_def = df_posse.loc[i]["Contatos", "Terço Def"]
    toque_meio = df_posse.loc[i]["Contatos", "Terço Central"]
    toque_ataque = df_posse.loc[i]["Contatos", "Terço de Ataque"]
    aprov_drible = df_posse.loc[i]["Dribles", "Suc%"]/10

    toques.append(toque)
    toques_def.append(toque_def)
    toques_meio.append(toque_meio)
    toques_ataque.append(toque_ataque)
    aprovs_dribles.append(aprov_drible)

nomes = ["Matheus Pereira", "Raphael Veiga"]

df_MP_veiga = pd.DataFrame({"Jogador": nomes,
                            "Jogos": jogos,
                            "Gols": gols,
                            "Assistencias":assists,
                            "Participações em Gols":participacoes,
                            "Chutes": chutes,
                            "Chutes para Marcar": chutes_para_marcar,
                            "Passes": passes,
                            "Aproveitamento de passes":aprovs_passes,
                            "Aproveitamento de passes curtos": aprovs_curto,
                            "Aproveitamento de passes medios": aprovs_medio,
                            "Aproveitamento de passes longos": aprovs_longo,
                            "Passes progressivos": passes_progressivos,
                            "Passes para chutes": passes_chute,
                            "Toques na bola": toques,
                            "Toques na defesa": toques_def,
                            "Toques no meio": toques_meio,
                            "Toques na ataque": toques_ataque,
                            "Aproveitamento de dribles": aprovs_dribles})

df_MP_veiga.to_csv("../Datasets/MP_Veiga.csv")



