import pandas as pd
import openpyxl
from openpyxl.chart import BarChart, Reference

# Função para extrair o tempo de execução (float)
def extrair_tempo_execucao(linha):
    try:
        return float(linha.strip())  # Converte a linha para float
    except ValueError:
        return None

# Função para extrair o uso de memória (int)
def extrair_memoria(linha):
    try:
        return int(linha.strip())  # Converte a linha para inteiro
    except ValueError:
        return None

# Abrir o arquivo .txt e ler as linhas
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
excel_path = 'resultados_com_grafico.xlsx'
df.to_excel(excel_path, index=False)

# Abrir o arquivo Excel gerado com openpyxl para adicionar o gráfico
wb = openpyxl.load_workbook(excel_path)
ws = wb.active

# Ajustar a largura das colunas para evitar sobreposição
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter  # Obter a letra da coluna
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2)  # Ajusta a largura da coluna
    ws.column_dimensions[column].width = adjusted_width

# Adicionar um gráfico de barras
chart = BarChart()
chart.title = "Tempo de Execução e Uso de Memória"
chart.style = 10  # Escolha o estilo do gráfico
chart.x_axis.title = 'Execuções'
chart.y_axis.title = 'Valores'

# Definir os dados do gráfico
data = Reference(ws, min_col=1, min_row=2, max_col=2, max_row=len(tempos_execucao)+1)
chart.add_data(data, titles_from_data=True)

# Definir as categorias (nomes das execuções)
categories = Reference(ws, min_col=1, min_row=2, max_row=len(tempos_execucao)+1)
chart.set_categories(categories)

# Posicionar o gráfico na planilha (por exemplo, na célula E5)
ws.add_chart(chart, "E1")

# Salvar as alterações no arquivo Excel
wb.save(excel_path)

print("Planilha criada com sucesso e gráfico adicionado!")
