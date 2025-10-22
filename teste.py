#pip install -r requirements.txt
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./dados/Mega-Sena.csv")

print(df.head())

# a parte que vai ser analisada
numeros = pd.concat([
    df["Bola1"], df["Bola2"], df["Bola3"],
    df["Bola4"], df["Bola5"], df["Bola6"]
])

contagem = numeros.value_counts().sort_index()

print("\n Números mais sorteados:")
print(contagem.sort_values(ascending=False).head(10))

plt.figure(figsize=(10, 5))
contagem.sort_values(ascending=False).head(10).plot(kind="bar", color="royalblue")
plt.title("10 Números Mais Sorteados na Mega-Sena")
plt.xlabel("Número")
plt.ylabel("Quantidade de vezes sorteado")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
