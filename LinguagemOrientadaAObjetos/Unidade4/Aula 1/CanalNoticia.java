
import java.util.ArrayList;
import java.util.List;

public class CanalNoticia {

    private List<Observador> observadores = new ArrayList<>();
    private String noticia;

    public void adcionarObservador(Observador o) {
        observadores.add(o);
    }

    public void removerObservador(Observador o) {
        observadores.remove(o);
    }

    public void novaNotica(String noticia) {
        this.noticia = noticia;
        notificarObservadores();
    }

    private void notificarObservadores() {
        for (Observador o : observadores) {
            o.atualizar(noticia);
        }
    }
}
