
public class Escola {

    public static void main(String[] args) {

        Aluno aluno1 = new Aluno("Victor", 1, 8);
        aluno1.exibirInformações();

        System.out.println("----------------------------");

        Avaliacao alunoGrad = new AlunoGraduacao("Lhaís", 2, 7);
        Avaliacao alunoProGrad = new AlunoPosGraduacao("Crisma", 3, 8);

        System.out.println("Média de Lhaís(Graduação)..." + alunoGrad.calcularMedia());
        System.out.println("Média de Crisma(PósGraduação)..." + alunoProGrad.calcularMedia());
    }
}
