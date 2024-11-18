import java.io.*;

public class Main {
    public static void main(String[] args) {
        try {
            // Lê o arquivo de entrada
            File arquivo = new File("arq-novo.txt");
            BufferedReader br = new BufferedReader(new FileReader(arquivo));

            LinkedList lista = new LinkedList();

            // Lê a linha de como a lista deve ser iniciada
            String linha = br.readLine().trim();  // Usando trim() para remover espaços extras
            String[] numerosIniciais = linha.split("\\s+");  // Usando \\s+ para dividir por espaços múltiplos
            for (String num : numerosIniciais) {
                lista.adicionarFinal(Integer.parseInt(num));  // Adiciona ao final da lista
            }

            // Lê a quantidade de ações
            linha = br.readLine().trim();  // Usando trim() para remover espaços extras
            int quantidadeAcoes = Integer.parseInt(linha);

            // Executa as ações
            for (int i = 0; i < quantidadeAcoes; i++) {
                linha = br.readLine().trim();  // Usando trim() para remover espaços extras

                // Verifica se a linha não está vazia antes de processá-la
                if (linha.isEmpty()) {
                    continue;  // Se a linha estiver vazia, pula para a próxima iteração
                }

                String[] acao = linha.split("\\s+");  // Usando \\s+ para dividir por espaços múltiplos

                // Ação de Adicionar (A) precisa de 3 parâmetros
                if (acao[0].equals("A") && acao.length == 3) {
                    int numero = Integer.parseInt(acao[1]);
                    int posicao = Integer.parseInt(acao[2]);
                    lista.adicionar(numero, posicao);
                }
                // Ação de Remover (R) precisa de 2 parâmetros
                else if (acao[0].equals("R") && acao.length == 2) {
                    int numero = Integer.parseInt(acao[1]);
                    lista.remover(numero);
                }
                // Ação de Imprimir (P) precisa de 1 parâmetro
                else if (acao[0].equals("P") && acao.length == 1) {
                    lista.imprimir();
                }
                else {
                    System.out.println("Ação inválida ou parâmetros incorretos: " + linha);
                }
            }

            br.close();

        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
        } catch (NumberFormatException e) {
            System.out.println("Erro ao converter número: " + e.getMessage());
        }
    }
}
