#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <chrono>
#include <thread>
#include <mutex>
#include <sys/resource.h>

using namespace std;

long getMemoryUsage() {
    struct rusage usage;
    getrusage(RUSAGE_SELF, &usage);
    return usage.ru_maxrss;
}

// Função para trocar dois elementos
void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

// Função de partição de Hoare
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[low];
    int i = low - 1;
    int j = high + 1;
    while (true) {
        do { i++; } while (arr[i] < pivot);
        do { j--; } while (arr[j] > pivot);
        if (i >= j) return j;
        swap(arr[i], arr[j]);
    }
}

// Função para o QuickSort, limitando o número de threads
void quickSort(vector<int>& arr, int low, int high, int max_depth) {
    if (low < high) {
        int pi = partition(arr, low, high);

        if (max_depth > 0) {
            // Usar uma nova thread para o QuickSort da parte esquerda
            thread leftThread([&]() {
                quickSort(arr, low, pi, max_depth - 1);
            });

            // Chamar o QuickSort na parte direita na thread principal
            quickSort(arr, pi + 1, high, max_depth - 1);

            // Esperar que a thread da esquerda termine
            leftThread.join();
        } else {
            // Quando a profundidade máxima for atingida, usar QuickSort de forma sequencial
            quickSort(arr, low, pi, 0);
            quickSort(arr, pi + 1, high, 0);
        }
    }
}

int main() {
    auto start = chrono::high_resolution_clock::now();

    ifstream file("arq.txt");
    if (!file) {
        cerr << "Erro ao abrir o arquivo!" << endl;
        return 1;
    }

    vector<int> arr;
    int num;
    while (file >> num) {
        arr.push_back(num);
    }
    file.close();

    srand(time(NULL));  // Garantir que a semente seja diferente a cada execução

    // Definir um limite de profundidade para o paralelismo
    int max_depth = 4;  // O número de threads paralelizadas, ajustável conforme necessário
    quickSort(arr, 0, arr.size() - 1, max_depth);

    ofstream outputFile("arq-saida.txt");
    if (!outputFile) {
        cerr << "Erro ao abrir o arquivo de saída!" << endl;
        return 1;
    }

    for (int i = 0; i < arr.size(); i++) {
        outputFile << arr[i] << endl;
    }
    outputFile.close();

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    cout << "Tempo de execução: " << duration.count() << " segundos" << endl;

     long finalMemory = getMemoryUsage();
    cout << "Uso de memória final: " << finalMemory << " KB" << endl;

    return 0;
}
