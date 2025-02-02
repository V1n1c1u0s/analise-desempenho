import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("--number", required=True)
args = parser.parse_args()

# Caminhos dos arquivos
arquivos = [f'time-{args.number}-heapsort.txt', f'time-{args.number}-quicksort.txt', f'time-{args.number}-mergesort.txt']

# Função para ler os tempos de execução dos arquivos, considerando apenas as linhas ímpares (1, 3, 5, 7,...)
def ler_tempos_arquivo(arquivo):
    if not os.path.exists(arquivo):
        print('Arquivo não existe')
        sys.exit()
    with open(arquivo, 'r') as file:
        # Lê todas as linhas
        linhas = file.readlines()
        # Pega as linhas ímpares (0, 2, 4,...)
        tempos = [float(linhas[i].strip()) for i in range(0, len(linhas), 2)]  # Pega as linhas 0, 2, 4, ..., até o fim
    return tempos

# Lê os tempos de cada arquivo
tempos_arquivo1 = ler_tempos_arquivo(arquivos[0])
tempos_arquivo2 = ler_tempos_arquivo(arquivos[1])
tempos_arquivo3 = ler_tempos_arquivo(arquivos[2])

# Verifica o número de tempos de cada arquivo
n = len(tempos_arquivo1)

# Configuração das posições das barras no eixo X
x = np.arange(n)  # Posições das barras (0 a n-1)
largura = 0.25  # Largura das barras

with PdfPages(f'{args.number}-num-grafico.pdf') as pdf:
    # Criação do gráfico de barras
    plt.figure(figsize=(10, 6))

    # Barras para cada arquivo (usando a posição deslocada para agrupamento)
    plt.bar(x - largura, tempos_arquivo1, largura, label=arquivos[0], color='skyblue')
    plt.bar(x, tempos_arquivo2, largura, label=arquivos[1], color='lightgreen')
    plt.bar(x + largura, tempos_arquivo3, largura, label=arquivos[2], color='salmon')

    # Adicionar título e rótulos aos eixos
    plt.title('Comparação dos Tempos de Execução', fontsize=14)
    plt.xlabel('Execuções', fontsize=12)
    plt.ylabel('Tempo de Execução (segundos)', fontsize=12)

    # Configuração do eixo X (com 10 linhas)
    plt.xticks(x, [f'Exec {i+1}' for i in range(n)])

    # Legenda
    plt.legend()

    # Exibir o gráfico
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    media_heapsort = np.mean(tempos_arquivo1)
    media_quicksort = np.mean(tempos_arquivo2)
    media_mergesort = np.mean(tempos_arquivo3)

    # Configuração do gráfico para as médias
    algoritmos = ['Heapsort', 'Quicksort', 'Mergesort']
    medias = [media_heapsort, media_quicksort, media_mergesort]

    # Criação do gráfico de barras para as médias
    plt.figure(figsize=(8, 5))

    # Barra para a média dos tempos
    plt.bar(algoritmos, medias, color=['skyblue', 'lightgreen', 'salmon'])

    # Adicionar título e rótulos aos eixos
    plt.title('Média dos Tempos de Execução', fontsize=14)
    plt.xlabel(f'{args.number} Números', fontsize=12)
    plt.ylabel('Média do Tempo de Execução (segundos)', fontsize=12)

    # Exibir o gráfico
    plt.tight_layout()
    pdf.savefig()
    plt.close()

    plt.figure(figsize=(10, 6))

    vencedor = medias.index(min(medias))

    texto = (
        f"Ganhador da Competição: {algoritmos[vencedor]}\n"
        f"Obteve o menor tempo de execução média. {medias[vencedor]} segundos"
    )

    plt.text(0.5, 0.5, texto, fontsize=12, ha='center', va='center', wrap=True)
    # Ajusta o layout e salva o texto como uma "página" no PDF
    plt.axis('off')  # Desativa os eixos, já que é apenas texto
    plt.tight_layout()
    pdf.savefig()
    plt.close()
