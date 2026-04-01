
import java.sql.Date;
import java.time.LocalDate;

public class SistemaBiblioteca {

    public static void main(String[] args) {
        //Datas automáticas usando Java 8+
        LocalDate hoje = LocalDate.now();
        LocalDate devolucao = hoje.plusDays(7);

        //Criando o objeto de empréstimo (Ex: Usuário 1 pegando Livro 1)
        Emprestimo novoEmprestimo = new Emprestimo(
                1,
                1,
                Date.valueOf(hoje),
                Date.valueOf(devolucao)
        );

        //Salvando no banco
        EmprestimoDAO dao = new EmprestimoDAO();
        dao.registrarEmprestimo(novoEmprestimo);
    }
}
