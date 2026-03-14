public class Cachorro extends Animal implements Treinavel {
    
    @Override
    public void falar(){
        System.out.println("O cachorro latiu");
    }

    @Override
    public void executarComando(String comando){
        System.out.println("O cacorro executou o comando" + comando);
    }
}
