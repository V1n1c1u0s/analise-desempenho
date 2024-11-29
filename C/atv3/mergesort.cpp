#include <iostream>
#include <vector>
#include <fstream>
#include <chrono>
#include <cstdlib>
#include <ctime>
#include <sys/resource.h>

using namespace std;

long getMemoryUsage() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    return usage.ru_maxrss;
}

// Função de merge para combinar duas metades ordenadas
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Vetores temporários
    vector<int> leftArr(n1), rightArr(n2);

    // Copiar os dados para os vetores temporários
    for (int i = 0; i < n1; i++) {
        leftArr[i] = arr[left + i];
    }
    for (int j = 0; j < n2; j++) {
        rightArr[j] = arr[mid + 1 + j];
    }

    // Mesclar os vetores temporários de volta para o vetor original
    int i = 0; 
    int j = 0; 
    int k = left; 

    while (i < n1 && j < n2) {
        if (leftArr[i] <= rightArr[j]) {
            arr[k] = leftArr[i];
            i++;
        } else {
            arr[k] = rightArr[j];
            j++;
        }
        k++;
    }

    // Copiar os elementos restantes do leftArr, se houver
    while (i < n1) {
        arr[k] = leftArr[i];
        i++;
        k++;
    }

    // Copiar os elementos restantes do rightArr, se houver
    while (j < n2) {
        arr[k] = rightArr[j];
        j++;
        k++;
    }
}

// Função recursiva de Merge Sort
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Ordenar as duas metades
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        // Combinar as metades ordenadas
        merge(arr, left, mid, right);
    }
}

int main() {
    // Medir o tempo de execução
    auto start = chrono::high_resolution_clock::now();

    ifstream file("arq.txt");
    if (!file) {
        cerr << "Erro ao abrir o arquivo!" << endl;
        return 1;
    }

    vector<int> arr;
    int num;
    while (file >> num) {
        arr.push_back(num);  // Lê os números do arquivo e armazena no vetor
    }
    file.close();

    // Chama o MergeSort
    mergeSort(arr, 0, arr.size() - 1);

    // Escrever os números ordenados em um arquivo de saída
    ofstream outputFile("arq-saida.txt");
    if (!outputFile) {
        cerr << "Erro ao abrir o arquivo de saída!" << endl;
        return 1;
    }

    for (int i = 0; i < arr.size(); i++) {
        outputFile << arr[i] << endl;  // Escreve os números ordenados no arquivo
    }
    outputFile.close();

    // Medir o tempo de execução após a ordenação
    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    cout << "Tempo de execução: " << duration.count() << " segundos" << endl;

    long finalMemory = getMemoryUsage();
    cout << "Uso de memória final: " << finalMemory << " KB" << endl;

    return 0;
}
