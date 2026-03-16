
public class Produto {

    //Atributos privados (encapsulados)
    private String nome;
    private double preco;
    private int quantidade;

    //Construtor para inicializar os atributos
    public Produto(String nome, double preco, int quantidade) {

        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    //Métodos de acesso (getters) para consultar os atributos
    public String getNome() {

        return nome;
    }

    public double getPreco() {

        return preco;
    }

    public int getQuantidade() {

        return quantidade;
    }

    //Métodos modificadores (setters) para alterar os atributos
    public void setPreco(double preco) {

        if (preco > 0) { //Validação para evitar valores inválidos
            this.preco = preco;
        }
    }

    public void setQuantidade(int quantidade) {

        if (quantidade >= 0) { //Validação para evitar estoques negativos
            this.quantidade = quantidade;
        }
    }

    //Método para exibir os detalhes do produto
    public void exibirDetalhes() {

        System.out.println("Produto: " + nome);
        System.out.println("Preço: R$ " + preco);
        System.out.println("Quantidade em Estoque: " + quantidade);
    }
}
