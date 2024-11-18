public class LinkedList {
    private Node head;

    // Construtor
    public LinkedList() {
        this.head = null;
    }

    // Adicionar um número na posição especificada
    public void adicionar(int numero, int posicao) {
        Node novoNo = new Node(numero);
        if (posicao == 0) {
            novoNo.next = head;
            head = novoNo;
            return;
        }

        Node temp = head;
        for (int i = 0; i < posicao - 1 && temp != null; i++) {
            temp = temp.next;
        }

        if (temp != null) {
            novoNo.next = temp.next;
            temp.next = novoNo;
        } else {
            System.out.println("Posição inválida para inserção");
        }
    }

    // Remover o primeiro nó encontrado com o valor especificado
    public void remover(int numero) {
        if (head == null) {
            System.out.println("Lista vazia!");
            return;
        }

        if (head.numero == numero) {
            head = head.next;
            return;
        }

        Node temp = head;
        while (temp.next != null && temp.next.numero != numero) {
            temp = temp.next;
        }

        if (temp.next != null) {
            temp.next = temp.next.next;
        } else {
            System.out.println("Número não encontrado!");
        }
    }

    // Imprimir a lista
    public void imprimir() {
        if (head == null) {
            System.out.println("Lista vazia!");
            return;
        }

        Node temp = head;
        while (temp != null) {
            System.out.print(temp.numero + " ");
            temp = temp.next;
        }
        System.out.println();
    }
}
