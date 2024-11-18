public class LinkedList {
    Node head;

    // Classe interna para representar um nó da lista
    private class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            this.next = null;
        }
    }

    // Método para adicionar um número na posição especificada
    public void adicionar(int numero, int posicao) {
        Node novoNo = new Node(numero);

        // Se a posição for 0, insere no início da lista
        if (posicao == 0) {
            novoNo.next = head;
            head = novoNo;
            return;
        }

        Node temp = head;
        // Percorre até o nó anterior à posição desejada
        for (int i = 0; temp != null && i < posicao - 1; i++) {
            temp = temp.next;
        }

        // Se a posição for válida (ou seja, temp não é null), insere o novo nó
        if (temp != null) {
            novoNo.next = temp.next;
            temp.next = novoNo;
        } else {
            System.out.println("Posição inválida para inserção");
        }
    }

    // Método para remover o primeiro nó com o valor especificado
    public void remover(int numero) {
        // Se a lista estiver vazia, retorna
        if (head == null) {
            return;
        }

        // Se o primeiro nó for o que queremos remover
        if (head.data == numero) {
            head = head.next;
            return;
        }

        // Percorre a lista procurando o nó a ser removido
        Node temp = head;
        while (temp.next != null && temp.next.data != numero) {
            temp = temp.next;
        }

        // Se encontrou o número, remove o nó
        if (temp.next != null) {
            temp.next = temp.next.next;
        }
    }

    // Método para imprimir a lista
    public void imprimir() {
        if (head == null) {
            System.out.println("Lista vazia");
            return;
        }

        Node temp = head;
        while (temp != null) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    // Método para adicionar ao final da lista (necessário para inicialização correta)
    public void adicionarFinal(int numero) {
        Node novoNo = new Node(numero);
        if (head == null) {
            head = novoNo;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = novoNo;
        }
    }
}
