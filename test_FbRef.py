import pandas as pd
import json
import requests

url = f"https://fbref.com/pt/partidas/7dee7a51/America-MG-Penarol-2023Abril5-Copa-Sudamericana"
response = requests.get(url)
html = response.content

tables = pd.read_html(html)

print(tables)


# gols = df["GP"]
# oponentes = df["Oponente"]

# plt.plot(oponentes, gols, marker="o", linestyle='-', color='b')

# plt.title("Gols X Adversários")
# plt.xlabel("Adversário")
# plt.ylabel("Gols")

# plt.xticks(rotation=45)

# plt.show()

