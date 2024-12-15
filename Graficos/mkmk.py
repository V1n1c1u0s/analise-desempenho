import pandas as pd
import openpyxl

def extrair_tempo_execucao(linha):
    try:
        return float(linha.strip())  # Converte a linha para float
    except ValueError:
        return None

def extrair_memoria(linha):
    try:
        return int(linha.strip())  # Converte a linha para inteiro
    except ValueError:
        return None

with open('test.txt', 'r') as f:
    linhas = f.readlines()

# Listas para armazenar os dados
tempos_execucao = []
usos_memoria = []

# Iterar pelas linhas do arquivo, processando os dados
for i in range(0, len(linhas), 2):  # Processando as linhas ímpares e pares
    tempo_execucao = extrair_tempo_execucao(linhas[i])  # A linha ímpar tem o tempo
    uso_memoria = extrair_memoria(linhas[i+1]) if i+1 < len(linhas) else None  # A linha par tem a memória

    if tempo_execucao is not None and uso_memoria is not None:
        tempos_execucao.append(tempo_execucao)
        usos_memoria.append(uso_memoria)

# Criar um DataFrame com os dados
df = pd.DataFrame({
    "Tempo de Execução (s)": tempos_execucao,
    "Uso de Memória (KB)": usos_memoria
})

# Salvar o DataFrame em uma planilha Excel
excel_path = 'resultados.xlsx'
df.to_excel(excel_path, index=False)

# Abrir o arquivo Excel gerado com openpyxl para ajustar a largura das colunas
wb = openpyxl.load_workbook(excel_path)
ws = wb.active

# Ajustar a largura das colunas com base no comprimento máximo de cada coluna
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  # Obter a letra da coluna
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width

# Salvar as alterações no arquivo Excel
wb.save(excel_path)
