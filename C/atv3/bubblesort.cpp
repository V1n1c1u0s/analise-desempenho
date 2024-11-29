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
    return usage.ru_maxrss;  // Retorna o uso máximo de memória em KB
}

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void bubbleSort(vector<int>& arr) {
    int n = arr.size();
    bool swapped;
    for (int i = 0; i < n - 1; i++) {
        swapped = false;
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]); 
                swapped = true;
            }
        }
        if (!swapped) break;
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

    bubbleSort(arr);

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
