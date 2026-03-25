
public class Instrutor {

    private String nome;
    private String email;
    private String areaEspecializacao;

    public Instrutor(String nome, String email, String areaEspecialização) {
        setNome(nome);
        setEmail(email);
        setAreaEspecializacao(areaEspecializacao);
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            throw new IllegalArgumentException("Erro: O nome do instrutor não pode ser vazio.");
        }
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        if (email != null && email.matches("^[A-Za-z0-9+_.-]+@(.+)$")) {
            this.email = email;
        } else {
            throw new IllegalArgumentException("Erro: Formato de e-mail inválido.");
        }
    }

    public String getAreaEspecialização() {
        return areaEspecializacao;
    }

    public void setAreaEspecializacao(String areaEspecializacao) {
        this.areaEspecializacao = areaEspecializacao;
    }
}
