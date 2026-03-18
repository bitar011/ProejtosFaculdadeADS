
public class AlunoGraduacao extends Aluno implements Avaliacao {

    public AlunoGraduacao(String nome, int matricula, double nota) {
        super(nome, matricula, nota);
    }

    @Override
    public double calcularMedia() {
        return getNota() * 1.0;
    }

}
