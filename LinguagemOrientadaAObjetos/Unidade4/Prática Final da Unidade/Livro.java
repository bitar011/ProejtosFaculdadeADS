public class Livro {
    //Atributos solicitados
    String titulo;
    String autor;
    int anoPublicacao;

    //Construtor para inicializar os dados
    public Livro(String titulo, String autor, int anoPublicacao) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
    }

    //Método para imprimir os dados do livro
    public void exibirInformacoes() {
        System.out.println("Título: " + titulo);
        System.out.println("Autor: " + autor);
        System.out.println("Ano: " + anoPublicacao);
        System.out.println("---------------------------");
    }
}