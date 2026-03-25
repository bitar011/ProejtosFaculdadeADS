
public class Curso {

    private String nomeCurso;
    private int cargaHoraria;
    private Instrutor instrutor;

    public Curso(String nome, int cargaHoraria, Instrutor instrutor) {
        setNomeCurso(nome);
        setCargaHoraria(cargaHoraria);
        setInstrutor(instrutor);
    }

    public String getNomeCurso() {
        return nomeCurso;
    }

    public void setNomeCurso(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            throw new IllegalArgumentException("Erro: O nome do curso não pode ser vazio.");
        }
        this.nomeCurso = nome;
    }

    public int getCargaHoraria() {
        return cargaHoraria;
    }

    public void setCargaHoraria(int cargaHoraria) {
        if (cargaHoraria <= 0) {
            throw new IllegalArgumentException("Erro: A carga horária dever ser maior que zero.");
        }
        this.cargaHoraria = cargaHoraria;
    }

    public Instrutor getInstrutor() {
        return instrutor;
    }

    public void setInstrutor(Instrutor instrutor) {
        if (instrutor == null) {
            throw new IllegalArgumentException("Erro: O curso deve ter um instrutor válido associado.");
        }
        this.instrutor = instrutor;
    }

    public void exibirDetalhes() {
        System.out.println("--- Detalhes do Curso ---");
        System.out.println("Curso: " + this.nomeCurso);
        System.out.println("Carga Horária: " + this.cargaHoraria + " horas");

        //Acessando os dados do objeto Instrutor associado a este curso
        System.out.println("Instrutor Responsável: " + this.instrutor.getNome());
        System.out.println("Contato do Instrutor: " + this.instrutor.getEmail());
        System.out.println("-------------------------\n");
    }
}
