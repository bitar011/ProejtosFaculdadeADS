
public class Principal {

    public static void main(String[] args) {
        OperacaoMatematica soma = new Soma();
        OperacaoMatematica divisao = new Divisao();

        //Teste da Soma
        try {
            System.out.println("Resultado da Soma: " + soma.calcular(10, 5));
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }

        //Teste da Divisão Correta
        try {
            System.out.println("Resultado da Divisão: " + divisao.calcular(10, 2));
        } catch (Exception e) {
            System.err.println(e.getMessage());
        }

        //Teste da Divisão por Zero (Tratamento de Exceção)
        try {
            System.out.println("Tentando dividir por zero...");
            System.out.println(divisao.calcular(10, 0));
        } catch (DivisaoPorZeroException e) {
            //Captura a exceção personalizada e exibe a mensagem configurada
            System.out.println("Capturado no Catch: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("Outro erro: " + e.getMessage());
        }
    }
}
