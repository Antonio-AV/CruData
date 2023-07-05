import pandas as pd
import json
import requests

url = f"https://fbref.com/pt/equipes/03ff5eeb/Cruzeiro-Estatisticas"
response = requests.get(url)
html = response.content

tables = pd.read_html(html)

print(tables[4])


# gols = df["GP"]
# oponentes = df["Oponente"]

# plt.plot(oponentes, gols, marker="o", linestyle='-', color='b')

# plt.title("Gols X Adversários")
# plt.xlabel("Adversário")
# plt.ylabel("Gols")

# plt.xticks(rotation=45)

# plt.show()

