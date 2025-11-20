import pandas as pd
import matplotlib.pyplot as plt

# === 1. Ler arquivo ===
df = pd.read_csv(".\dados\original.csv", sep=r'\s*;\s*')
df.columns = df.columns.str.strip()

# === 2. Criar a razão mulheres/homens ===
df["Razao_Mulher_Homem"] = df["Mulheres/2022"] / df["Homens/2022"]

# === 3. Selecionar apenas o Top 5 mais femininos ===
top5_mulher_relativa = df.sort_values(by="Razao_Mulher_Homem", ascending=False).head(6)

# === 4. Preparar dados ===
bairros = top5_mulher_relativa["bairro"].tolist()
homens = top5_mulher_relativa["Homens/2022"].tolist()
mulheres = top5_mulher_relativa["Mulheres/2022"].tolist()
ratio = top5_mulher_relativa["Razao_Mulher_Homem"].tolist()

x = list(range(len(bairros)))
width = 0.25

# === 5. Gráfico Clustered Column + Line ===
plt.figure(figsize=(12, 7))

plt.bar([i - width/2 for i in x], homens, width, label="Homens")
plt.bar([i - width/2 for i in x], mulheres, width, bottom=homens, label="Mulheres")

plt.plot(x, ratio, marker="o", color="black", linewidth=2,
         label="Proporção Mulheres/Homens")

plt.xticks(x, bairros, rotation=45, ha="right")
plt.ylabel("População / Proporção")
plt.title("Top 5 Bairros mais Femininos — Proporção Mulheres/Homens")
plt.grid(axis="y", linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()
