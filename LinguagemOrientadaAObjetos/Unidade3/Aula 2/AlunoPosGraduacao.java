
public class AlunoPosGraduacao extends Aluno implements Avaliacao {

    public AlunoPosGraduacao(String nome, int matricula, double nota) {
        super(nome, matricula, nota);

    }

    @Override
    public double calcularMedia() {
        return getNota() * 1.2;
    }

}
