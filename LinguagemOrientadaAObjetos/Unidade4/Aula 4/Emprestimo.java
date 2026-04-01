
import java.sql.Date;

public class Emprestimo {

    private int idUsuario;
    private int idLivro;
    private Date dataEmprestimo;
    private Date dataDevolucaoPrevista;

    //Construtor
    public Emprestimo(int idUsuario, int idLivro, Date dataEmprestimo, Date dataDevolucaoPrevista) {
        this.idUsuario = idUsuario;
        this.idLivro = idLivro;
        this.dataEmprestimo = dataEmprestimo;
        this.dataDevolucaoPrevista = dataDevolucaoPrevista;
    }

    //Getters
    public int getIdUsuario() {
        return idUsuario;
    }

    public int getIdLivro() {
        return idLivro;
    }

    public Date getDataEmprestimo() {
        return dataEmprestimo;
    }

    public Date getDataDevolucaoPrevista() {
        return dataDevolucaoPrevista;
    }
}
