import java.util.Scanner;

public class GerenciamentoNotas{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        double[] notas = new double[5];

        //Inserir notas
        System.out.println("Insira as notas dos alunos:");
        for(int i = 0; i < notas.length; i++){
            System.out.println("Nota do aluno " + (i+1) + ": ");
            notas[i] = scanner.nextDouble();
        }

        //Atualizar nota especifica
        System.out.println("\nDigite o índice do aluno para atualizar a nota(1 a 5): ");
        int indice = scanner.nextInt() - 1;
        if(indice >= 0 && indice < notas.length){
            System.out.println("Digite a nova nota: ");
            notas[indice] = scanner.nextDouble();
        } else{
            System.out.println("Índice inválido!");
        }

        //Calcular méida das notas
        double soma = 0;
        for (double nota : notas){
            soma += nota;
        }
        double media = soma / notas.length;
        System.out.printf("\nMédia da turma: %.2f\n", media);

        //Encontrar a maior e menor nota
        double maior = notas[0], menor = notas[0];
        for(double nota : notas){
            if(nota > maior) maior = nota;
            if(nota < menor) menor = nota;
        }
        System.out.printf("Maior nota: %.2f\n", maior);
        System.out.printf("Menor nota: %.2f\n", menor);


        scanner.close();
    }
}