import pandas as pd
import matplotlib.pyplot as plt

# === 1. Ler o arquivo ===
df = pd.read_csv("./dados/mapa(2).csv")
df.columns = df.columns.str.strip().str.replace('"', '')
# === 2. Definir colunas ===
local = "Local"
col_salario = "Salário médio mensal dos trabalhadores formais"

# === 3. Converter valores para número (salário mínimo → reais)
df[col_salario] = (
    df[col_salario]
    .astype(str)
    .str.replace(",", ".")
    .str.replace(r"[^\d\.]", "", regex=True)
    .astype(float)
)

# Converte de salários mínimos para reais (usando salário mínimo de 2022 = R$ 1.212)
SALARIO_MINIMO_2022 = 1212
df["Salário (R$)"] = df[col_salario] * SALARIO_MINIMO_2022

# === 4. Ordenar ===
df_sorted = df.sort_values(by="Salário (R$)", ascending=False)

# Selecionar top 10 e bottom 10
top10 = df_sorted.head(10)
bottom10 = df_sorted.tail(10)

# === 5. Unir ===
combined = pd.concat([top10, bottom10])

# === 6. Gráfico ===
plt.figure(figsize=(10, 8))
bars = plt.barh(
    combined[local],
    combined["Salário (R$)"],
    color=["#2ca02c" if i < 10 else "#d62728" for i in range(len(combined))]
)
plt.gca().invert_yaxis()

plt.title("Locais com Maior e Menor Salário Médio Mensal (R$)", fontsize=14, fontweight="bold")
plt.xlabel("Salário médio mensal (R$)")
plt.ylabel("Local")
plt.grid(axis="x", linestyle="--", alpha=0.5)

# === 7. Adiciona labels nas barras ===
max_val = combined["Salário (R$)"].max()
for bar in bars:
    valor = bar.get_width()
    percentual = (valor / max_val) * 100
    plt.text(valor + (max_val * 0.01),
             bar.get_y() + bar.get_height() / 2,
             f"R${valor:,.0f}",
             va="center", fontsize=9)

plt.tight_layout()
plt.show()

# === 8. Mostrar os dados no terminal ===
print("\n🏆 Top 10 Locais com Maior Salário Médio:")
print(top10[[local, "Salário (R$)"]])

print("\n⚠️ Top 10 Locais com Menor Salário Médio:")
print(bottom10[[local, "Salário (R$)"]])
