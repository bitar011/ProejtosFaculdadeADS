
public class Produto {

    private String nome;
    private double preco;
    private static int quantidadeTotal = 0;

    //Construrtor padrão
    public Produto() {
        this.nome = "Indefinido";
        this.preco = 0.0;
        quantidadeTotal++;
    }

    //Construrtor com parâmetros (Sobrecarga)
    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
        quantidadeTotal++;
    }

    //Método para exibir os dados do produtos
    public void exibirDados() {
        System.out.println("Produto: " + nome + " | Preço: R$ " + preco);
    }

    //Método estático para exibir o total
    public static void exibirQuantidadeTotal() {
        System.out.println("Quantidade total de produtos cadastrados: " + quantidadeTotal);
    }
}
