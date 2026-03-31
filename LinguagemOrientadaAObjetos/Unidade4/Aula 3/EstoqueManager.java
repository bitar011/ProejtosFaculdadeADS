import java.io.*;
import java.util.*;

public class EstoqueManager{

    private static final String ARQUIVO_ESTOQUE = "estoque.txt";

    public static void main(String[] args) throws IOException{
        //Exemplo de uso
        adicionarProduto("001", "Martelo", 8, 25.50);
        adicionarProduto("002", "Chave de Fenda", 15, 12.00);
        exibirEstoque();
        atualizarProduto("001", 10, 26.00);
        gerarRelatorioEstoqueBaixo();
    }

    //Método para adicionar um produto no arquivo
    public static void adicionarProduto(String codigo, String descricao, int quantidade, double preco) throws IOException{
        if(produtoExiste(codigo)){
            System.out.println("Produto com código " + codigo + "já existe.");
            return;
        }

        try(BufferedWriter writer = new BufferedWriter(new FileWriter(ARQUIVO_ESTOQUE, true))){
            writer.write(codigo + " | " + descricao + " | " + quantidade + " | " + preco);
            writer.newLine();
        }
        System.out.println("Produto adicionado: " + descricao);
    }

    //Método para verificar se um produto ja existe no arquivo
    private static boolean produtoExiste(String codigo) throws IOException {
        try(BufferedReader reader = new BufferedReader(new FileReader(ARQUIVO_ESTOQUE))){
            String linha;
            while ((linha = reader.readLine()) != null){
                String[] partes = linha.split(" \\|");
                if(partes[0].equals(codigo)){
                    return true;
                }
            }
        }
        return false;
    }

    //Método para exibir os produtos no estoque
    public static void exibirEstoque() throws IOException{
        System.out.println("Estoque Atual:");
        try(BufferedReader reader = new BufferedReader(new FileReader(ARQUIVO_ESTOQUE))){
            String linha;
            while((linha = reader.readLine()) != null){
                System.out.println(linha);
            }
        }
    }

    //Método para atualizar um produto no arquivo
    public static void atualizarProduto(String codigo, int novaQuantidade, double novoPreco) throws IOException {
        File arquivo = new File(ARQUIVO_ESTOQUE);
        File arquivoTemp = new File("estoque_temp.txt");

        try(BufferedReader reader = new BufferedReader(new FileReader(arquivo));
        BufferedWriter writer = new BufferedWriter(new FileWriter(arquivoTemp))){
            
            String linha;
            boolean produtoAtualizado = false;

            while((linha = reader.readLine()) != null){
                String[] partes = linha.split(" \\| ");
                if(partes[0].equals(codigo)){
                    linha = codigo + " | " + partes[1] + " | " + novaQuantidade + " | " + novoPreco;
                    produtoAtualizado = true;
                }
                writer.write(linha);
                writer.newLine();
            }

            if(!produtoAtualizado){
                System.out.println("Produto com código " + codigo + "não encontrado.");
            }
        }
        arquivo.delete();
        arquivoTemp.renameTo(arquivo);
        System.out.println("Produto atualizado com sucesso.");
    }

    //Método para gerar relatorio de produtos com estoque baixo
    public static void gerarRelatorioEstoqueBaixo() throws IOException {
        System.out.println("Relatório de Estoque Baixo:");
        try(BufferedReader reader = new BufferedReader(new FileReader(ARQUIVO_ESTOQUE))){
            String linha;
            while((linha = reader.readLine()) != null){
                String[] partes = linha.split(" \\| ");
                int quantidade = Integer.parseInt(partes[2].trim());
                if (quantidade < 5){
                    System.out.println(linha);
                }
            }
        }
    }   
}