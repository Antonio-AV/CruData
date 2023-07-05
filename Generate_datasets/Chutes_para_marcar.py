import pandas as pd
import json

# VISITA AS PAGINAS INICIAIS DE ESTATISTICAS DE CADA TIME BRASILEIRO E FILTRA AS INFORMAÇÕES DO NOME DO JOGADOR, TEMPO DE JOGO(MIN), GOLS E POSIÇÃO

test = open('../times_brasileirao.json')
data = json.load(test)

df_chutes_para_marcar = pd.DataFrame()

for i in range(len(data["Times"])):
    time = data["Times"][i]["Time"]
    id = data["Times"][i]["id"]

    url = f"https://fbref.com/pt/equipes/{id}/{time}-Estatisticas"
    df = pd.read_html(url)[4]
    #print(df)

    nomes = []
    chutes = []
    gols = []
    posicoes = []
    for j in range(len(df["Unnamed: 0_level_0"])-2):
        jogador = df.loc[j, "Unnamed: 0_level_0"]
        nome = jogador.Jogador
        chute = df["Padrão", "TC"][j]
        gol = df["Padrão", "Gols"][j]
        posicao = df["Unnamed: 2_level_0", "Pos."][j]
        nomes.append(nome)
        chutes.append(chute)
        gols.append(gol)
        posicoes.append(posicao)
    df_chutes_para_marcar_time = pd.DataFrame({"Jogador": nomes,
                                                "Chutes": chutes,
                                                "Gols": gols,
                                                "Time":time,
                                                "Posicao":posicoes})
    df_chutes_para_marcar_time = df_chutes_para_marcar_time.dropna()
    df_chutes_para_marcar_time = df_chutes_para_marcar_time.drop(df_chutes_para_marcar_time[df_chutes_para_marcar_time["Chutes"] == 0].index)
    df_chutes_para_marcar_time = df_chutes_para_marcar_time.drop(df_chutes_para_marcar_time[df_chutes_para_marcar_time["Gols"] == 0].index)
    print(df_chutes_para_marcar_time)
    df_chutes_para_marcar = pd.concat([df_chutes_para_marcar, df_chutes_para_marcar_time])
        
df_chutes_para_marcar = df_chutes_para_marcar.reset_index(drop=True)
print(df_chutes_para_marcar)

df_chutes_para_marcar.to_csv("../Datasets/Chutes_para_marcar.csv")
