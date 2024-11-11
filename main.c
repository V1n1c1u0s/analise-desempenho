#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct No {
    int valor;
    struct No* prox;
} No;

No* criarNo(int valor);
void addNo(No** nums, int valor, int pos);
void removeNo(No** nums, int valor);
void printList(No* nums);
void valoresIniciais(No** nums, char* linha);
void iniciarLista(FILE* fl, No** nums);


int main(){
    FILE* fl = fopen("arq.txt", "r");
    FILE* fl = fopen("arq2.txt", "r");

    if(fl == NULL){
        printf("\n\nErro ao abrir\n\n");
        return 1;
    }

    No* nums = NULL;
    No* nums2 = NULL;
    iniciarLista(fl, &nums);
    printf("\n\n---------------------------------------------\n\n");
    iniciarLista(fl2, nums2)
    fclose(fl);
    fclose(fl2);
    return 0;
}


No* criarNo(int valor){
    No* novoNo = (No*)malloc(sizeof(No));
    novoNo->valor = valor;
    novoNo->prox = NULL;
    return novoNo;
}

void addNo(No** nums, int valor, int pos){
    No* novoNo = criarNo(valor);

    if(*nums == NULL || pos == 0){
        novoNo->prox = *nums;
        *nums = novoNo;
        return;
    }
    No* temp = *nums;

    if(pos == -1){
        while(temp->prox != NULL) temp = temp->prox;
        novoNo->prox = temp->prox;
        temp->prox = novoNo;
        return;
    }

    int posAtual = 0;

    while(temp->prox != NULL && posAtual < pos - 1){
        temp = temp->prox;
        posAtual++;
    }
    // Insere no fim caso a pos ultrapasse o limite
    novoNo->prox = temp->prox;
    temp->prox = novoNo;
}

void removeNo(No** nums, int valor){
    if (*nums == NULL) return; 

    No* temp = *nums;
    No* ant = NULL;

    if(temp != NULL && temp->valor == valor){
        *nums = temp->prox;
        free(temp);
        return;
    }

    while(temp != NULL && temp->valor != valor){
        ant = temp;
        temp = temp->prox;
    }

    if(temp == NULL) return;

    ant->prox = temp->prox;
    free(temp);
}

void printList(No* nums){
    if(nums == NULL){
        printf("\n\nLista Vazia\n\n");
        return;
    }

    No* temp = nums;
    while(temp != NULL){
        printf("%d ", temp->valor);
        temp = temp->prox;
    }
    printf("\n");
}

void valoresIniciais(No** nums, char* linha){
    int num;
    char* start = linha;
    while(sscanf(start, "%d", &num) == 1){
        addNo(nums, num, -1);
        while (*start && *start != ' ') start++;
        if (*start) start++;
    }
}

void iniciarLista(FILE* fl, No** nums){
    char linha[1024];

    if(fgets(linha, sizeof(linha), fl)) valoresIniciais(nums, linha);

    while(fgets(linha, sizeof(linha), fl)){
        char comando;
        int valor, pos;

        // Ignora td q tiver apenas 1 número
        if(sscanf(linha, "%d", &valor) == 1){
            continue; 
        }

        if(sscanf(linha, "%c", &comando) == 1){
            switch(comando){
                case 'A':  // Adiciona No
                    if(sscanf(linha + 2, "%d %d", &valor, &pos) == 2){
                        addNo(nums, valor, pos);
                    } else{
                        addNo(nums, valor, -1);  //Adiciona no final
                    }
                    break;
                case 'R':  // Remove No
                    if(sscanf(linha + 2, "%d", &valor) == 1){
                        removeNo(nums, valor);
                    }
                    break;
                case 'P':  
                    printList(*nums);
                    break;
                default:
                    printf("\n\nEsse comando nao existe: %c\n\n", comando);
                    break;
            }
        }
    }
}