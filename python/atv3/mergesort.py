import time
import psutil
import os

# Obtendo o processo atual
process = psutil.Process(os.getpid())

# Inicia o temporizador
start_time = time.time()

# Obtendo o uso de memória antes da execução
memory_before = process.memory_info().rss / 1024  # Em KB

def merge(arr, l, m, r):
	n1 = m - l + 1
	n2 = r - m

	L = [0] * (n1)
	R = [0] * (n2)

	for i in range(0, n1):
		L[i] = arr[l + i]

	for j in range(0, n2):
		R[j] = arr[m + 1 + j]

	i = 0
	j = 0
	k = l

	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2

		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)


with open('arq.txt', 'r') as file:
    arr = list(map(int, file.read().splitlines()))

n = len(arr)

mergeSort(arr, 0, n-1)

with open('arq-saida.txt','w') as file:
    for i in arr:
        file.write(f'{i}\n')
		
end_time = time.time()

# Obtendo o uso de memória após a execução do código
memory_after = process.memory_info().rss / 1024  # Em KB

# Calcula o tempo de execução
execution_time = end_time - start_time

# Calcula o uso de memória
memory_usage = memory_after - memory_before

print(f"Tempo de execução: {execution_time:.6f} segundos")
print(f"Uso de memória durante a execução: {memory_usage:.2f} KB")