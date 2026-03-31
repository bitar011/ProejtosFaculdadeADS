public class ArrayUnidimensional{
    public static void main(String[] args) {
        int[] notas = new int[5];
        notas[0] = 85;
        notas[1] = 90;
        notas[2] = 78;
        notas[3] = 88;
        notas[4] = 92;

        for(int i = 0; i < notas.length; i++){
            System.out.println("Nota do aluno " + (i + 1) + ": " + notas[i]);
        }
    }
}