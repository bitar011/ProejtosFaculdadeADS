
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class EmprestimoDAO {

    public void registrarEmprestimo(Emprestimo emp) {
        String sql = "INSERT INTO Emprestimo (id_usuario, id_livro, data_emprestimo, data_devolucao_prevista) VALUES (?, ?, ?, ?)";

        try (Connection conn = ConexaoBanco.conectar(); PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setInt(1, emp.getIdUsuario());
            stmt.setInt(2, emp.getIdLivro());
            stmt.setDate(3, emp.getDataEmprestimo());
            stmt.setDate(4, emp.getDataDevolucaoPrevista());

            stmt.executeUpdate();
            System.out.println("Empréstimo registrado com sucesso!");

        } catch (SQLException e) {
            System.err.println("Erro ao registrar empréstimo: " + e.getMessage());
        }
    }
}
