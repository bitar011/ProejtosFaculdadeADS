
class Aluno extends Pessoa {

    private int matricula;

    public Aluno(String nome, int matricula) {
        super(nome);
        this.matricula = matricula;
    }

    @Override
    public void apresentar() {
        System.out.println("Eu sou o aluno: " + nome + " e minha matricula é " + matricula);
    }

}
