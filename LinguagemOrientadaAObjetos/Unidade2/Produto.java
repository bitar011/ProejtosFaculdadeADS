public class Produto {
    String nome;
    double preco;

    public Produto(String nome, double preco){
        this.nome = nome;
        this.preco = preco;
    }

    public Produto(String nome){
        this.nome = nome;
        this.preco = 10.00;
    }

    public void exibirDetalhes(){
        System.out.println("Produto:" + nome + ", Preço: R$" + preco);
    }

    public static void main(String[] args) {
        Produto p1 = new Produto("Bolo de Chocolate", 35.00);
        Produto p2 = new Produto("Brownie");

        p1.exibirDetalhes();
        p2.exibirDetalhes();
    }
    //javac "nomeDoArquivo".java -- para compilar
    //java "nomeDoArquivo" -- para rodar arquivo compilado

}
