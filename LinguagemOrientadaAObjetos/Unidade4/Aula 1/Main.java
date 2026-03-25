
public class Main {

    public static void main(String[] args) {
        System.out.println("Padrão observer");

        CanalNoticia canal = new CanalNoticia();
        Usuario usuario1 = new Usuario("Victor Bitar");
        Usuario usuario2 = new Usuario("Gustavo");

        canal.adcionarObservador(usuario1);
        canal.adcionarObservador(usuario2);

        canal.novaNotica("Novo produto lançado!");
    }
}
