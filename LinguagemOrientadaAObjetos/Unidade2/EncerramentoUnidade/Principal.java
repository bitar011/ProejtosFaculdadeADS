
public class Principal {

    public static void main(String[] args) {
        //Instanciando três objetos com construtores diferentes
        Produto p1 = new Produto("Notebook", 3500.00);
        Produto p2 = new Produto("Mouse Gamer", 150.00);
        Produto p3 = new Produto(); //Utilizando construtor padrão

        //Exibindo dados de cada produto
        p1.exibirDados();
        p2.exibirDados();
        p3.exibirDados();

        System.out.println("--------------------------------"); //Linha divisória para clareza no console

        Produto.exibirQuantidadeTotal();
    }
}
