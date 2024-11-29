#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <chrono>
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

// Função do QuickSort sequencial
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        // Recursão nas duas metades
        quickSort(arr, low, pi);
        quickSort(arr, pi + 1, high);
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

    // Chamar o QuickSort sequencial
    quickSort(arr, 0, arr.size() - 1);

    ofstream outputFile("arq-saida.txt");
    if (!outputFile) {
        cerr << "Erro ao abrir o arquivo de saída!" << endl;
        return 1;
    }

    // Escrever o array ordenado no arquivo de saída
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
