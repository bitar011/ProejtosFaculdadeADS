
class Aluno {

    private String nome;
    private int matricula;
    private double nota;

    public Aluno(String nome, int matricula, double nota) {
        this.nome = nome;
        this.matricula = matricula;
        setNota(nota);

    }

    public void setNota(double nota) {
        try {
            if (nota < 0 || nota > 10) {
                throw new IllegalArgumentException("Nota inválida! Deve estar entre 0 e 10");

            }
            this.nota = nota;
        } catch (IllegalArgumentException e) {
            System.out.println("Erro: " + e.getMessage());
        } finally {
            System.out.println("Operação Finalizada.");
        }
    }

    public void exibirInformações() {
        System.out.println("Nome: " + nome + ", Matricula: " + matricula + ", Nota: " + nota);
    }
}
