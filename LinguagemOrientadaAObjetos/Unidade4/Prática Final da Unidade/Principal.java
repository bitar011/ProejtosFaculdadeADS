
public class Principal {

    public static void main(String[] args) {
        //Declaração de um array de 5 objetos Livro
        Livro[] livros = new Livro[5];

        //Preenchimento direto do array utilizando o construtor
        livros[0] = new Livro("Java: Como Programar", "Deitel", 2017);
        livros[1] = new Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954);
        livros[2] = new Livro("Estruturas de Dados em Java", "Loiane Groner", 2019);
        livros[3] = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        livros[4] = new Livro("Aprendendo Java Moderno", "Claudio de Castro", 2021);

        System.out.println("=== Livros que contêm 'Java' no título ===\n");

        //Laço for para percorrer o array
        for (int i = 0; i < livros.length; i++) {
            //Filtragem utilizando o método contains() da classe String
            if (livros[i].titulo.contains("Java")) {
                livros[i].exibirInformacoes(); //Exibe apenas se o critério for atendido
            }
        }
    }
}
