#pip install -r requirements.txt
import pandas as pd

# Lê o arquivo CSV
df = pd.read_csv("./dados/Mega-Sena.csv")

# Mostra as primeiras linhas pra você conferir a estrutura
print(df.head())

# Junta todos os números em uma única série (coluna)
# — substitua aqui pelos nomes reais das colunas do seu arquivo
numeros = pd.concat([
    df["Bola1"], df["Bola2"], df["Bola3"],
    df["Bola4"], df["Bola5"], df["Bola6"]
])

# Conta quantas vezes cada número aparece
contagem = numeros.value_counts().sort_index()

# Mostra os 10 números mais sorteados
print("\n🎲 Números mais sorteados:")
print(contagem.sort_values(ascending=False).head(10))

# (Opcional) Mostra em gráfico de barras
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 5))
contagem.sort_values(ascending=False).head(10).plot(kind="bar", color="royalblue")
plt.title("10 Números Mais Sorteados na Mega-Sena")
plt.xlabel("Número")
plt.ylabel("Quantidade de vezes sorteado")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
