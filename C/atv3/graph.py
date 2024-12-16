import time
import psutil
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

# Função para medir o tempo de execução e o consumo de memória
def medir_execucao(linguagem, programa):
    # Compilar o programa C++ antes de executá-lo
    if linguagem == 'cpp':
        subprocess.run(["g++", programa, "-o", "programa"])

    # Medir o tempo de execução
    start_time = time.time()

    # Iniciar o subprocesso e monitorar a memória
    if linguagem == 'cpp':
        processo = subprocess.Popen(["./programa"])

    # Usar psutil para monitorar o processo filho
    processo_ps = psutil.Process(processo.pid)
    
    # Medir a memória antes da execução
    memoria_antes = processo_ps.memory_info().rss / 1024  # Convertendo para KB

    # Esperar o processo terminar e capturar o tempo
    processo.wait()

    # Medir o tempo de execução
    tempo_execucao = time.time() - start_time
    
    # Medir o consumo de memória depois da execução
    memoria_depois = processo_ps.memory_info().rss / 1024  # Convertendo para KB
    memoria_usada = memoria_depois - memoria_antes
    
    return tempo_execucao, memoria_usada

# Função para rodar o programa 10 vezes e gerar as estatísticas
def rodar_algoritmo(linguagem, programa):
    tempos_execucao = []
    memorias_usadas = []
    
    # Rodar o programa 10 vezes
    for i in range(10):
        tempo, memoria = medir_execucao(linguagem, programa)
        tempos_execucao.append(tempo)
        memorias_usadas.append(memoria)
    
    return tempos_execucao, memorias_usadas

# Função para gerar os gráficos e salvar os resultados em uma planilha
def gerar_graficos_e_planilha(algoritmo, tempos_execucao, memorias_usadas):
    # Calcular média e mediana
    media_tempo = np.mean(tempos_execucao)
    mediana_tempo = np.median(tempos_execucao)

    media_memoria = np.mean(memorias_usadas)
    mediana_memoria = np.median(memorias_usadas)

    # Exibir os resultados
    print(f'{algoritmo} - Média do tempo de execução: {media_tempo:.4f} segundos')
    print(f'{algoritmo} - Mediana do tempo de execução: {mediana_tempo:.4f} segundos')
    print(f'{algoritmo} - Média do consumo de memória: {media_memoria:.4f} KB')
    print(f'{algoritmo} - Mediana do consumo de memória: {mediana_memoria:.4f} KB')

    # Criar um DataFrame com os resultados
    df = pd.DataFrame({
        'Execução': range(1, 11),
        'Tempo (segundos)': tempos_execucao,
        'Memória (KB)': memorias_usadas
    })

    # Salvar os resultados em uma planilha Excel
    df.to_excel(f'resultados_{algoritmo}.xlsx', index=False)

    # Gráficos

    # Gráfico de Tempo de Execução
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), tempos_execucao, marker='o', color='b', label='Tempo de Execução (segundos)')
    plt.axhline(media_tempo, color='r', linestyle='--', label=f'Média Tempo: {media_tempo:.4f}')
    plt.axhline(mediana_tempo, color='g', linestyle='-.', label=f'Mediana Tempo: {mediana_tempo:.4f}')
    plt.xlabel('Execuções')
    plt.ylabel('Tempo (segundos)')
    plt.title(f'Tempo de Execução do {algoritmo}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'grafico_{algoritmo}_tempo.png')
    plt.show()

    # Gráfico de Consumo de Memória
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 11), memorias_usadas, marker='o', color='b', label='Consumo de Memória (KB)')
    plt.axhline(media_memoria, color='r', linestyle='--', label=f'Média Memória: {media_memoria:.4f}')
    plt.axhline(mediana_memoria, color='g', linestyle='-.', label=f'Mediana Memória: {mediana_memoria:.4f}')
    plt.xlabel('Execuções')
    plt.ylabel('Memória (KB)')
    plt.title(f'Consumo de Memória do {algoritmo}')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'grafico_{algoritmo}_memoria.png')
    plt.show()

# Algoritmos a serem testados e suas linguagens
algoritmos = [
    ('bubblesort', 'cpp', 'bubblesort.cpp'),
    ('quicksort', 'cpp', 'quicksort.cpp'),
    ('mergesort', 'cpp', 'mergesort.cpp'),
]

# Rodar os testes para cada algoritmo
for algoritmo, linguagem, programa in algoritmos:
    print(f"Executando o algoritmo {algoritmo} na linguagem {linguagem}...")
    tempos_execucao, memorias_usadas = rodar_algoritmo(linguagem, programa)
    gerar_graficos_e_planilha(algoritmo, tempos_execucao, memorias_usadas)
