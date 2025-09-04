import matplotlib.pyplot as plt

# Ler os resultados do arquivo gerado pelo MRJob
resultados = {}
with open('resultados.txt', 'r') as f:
    for linha in f:
        try:
            palavra, qtd = linha.strip().split('\t')
            palavra = palavra.strip('"')  # remover aspas
            qtd = int(qtd)
            resultados[palavra] = (qtd)
        except ValueError:
            print(f"[AVISO] Linha ignorada (não é número): {linha.strip()}")
        except Exception as e:
            print(f"[ERRO] Linha inválida: {linha.strip()} ({e})")

# (Opcional) Ordenar por frequência
resultados_ordenados = dict(sorted(resultados.items(), key=lambda item: item[1], reverse=True))

# (Opcional) Limitar para as 10 palavras mais frequentes
top_palavras = dict(list(resultados_ordenados.items())[:10])

# Dados para o gráfico
palavras = list(top_palavras.keys())
frequencias = list(top_palavras.values())

# Plotar com matplotlib
plt.figure(figsize=(10, 6))
plt.bar(palavras, frequencias, color='royalblue')
plt.title('Top 10 Palavras Mais Frequentes')
plt.xlabel('Palavras')
plt.ylabel('Frequência')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
