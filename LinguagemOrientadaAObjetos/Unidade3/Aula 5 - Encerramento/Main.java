
public class Main {

    public static void main(String[] args) {
        try {
            //Criando o instrutor com dados válidos
            Instrutor instrutor1 = new Instrutor("Bruno", "brunosilva@email.com", "Desenvolvimento Back-end");

            //Criando o curso e associando o instrutor
            Curso curso1 = new Curso("Lógica de Programação", 40, instrutor1);

            //Exibindo os detalhes
            curso1.exibirDetalhes();

            //Testando a validação: Tentando alterar o e-mail para um formato inválido
            System.out.println("Tentando atualizar e-mail para um formato incorreto...");
            instrutor1.setEmail("brunosilva_sem_arroba.com"); //Isso vai disparar a exceção

        } catch (IllegalArgumentException e) {
            //Captura e exibe a mensagem de erro da validação
            System.out.println(e.getMessage());
        }
    }
}
