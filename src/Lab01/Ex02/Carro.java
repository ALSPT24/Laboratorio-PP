package Lab01.Ex02;

public class Carro {
    private final String matricula;
    private int velocidadeAtual;
    private final int velocidadeMaxima = 200;
    private boolean ligado;
    private final Condutor conductor;

    public Carro(String matricula, Condutor conductor) {
        this.matricula = matricula;
        this.conductor = conductor;
        this.ligado = false;
        this.velocidadeAtual = 0;
    }

    public void ligar() {
        ligado = true;
        System.out.println("Carro " + matricula + " ligado.");
    }

    public void desligar() {
        ligado = false;
        System.out.println("Carro " + matricula + " desligado.");
    }

    public void acelerar() {
        if (!ligado) {
            System.out.println("O carro está desligado! Não pode acelerar.");
            return;
        }
        velocidadeAtual += 10;
        if (velocidadeAtual > velocidadeMaxima)
            velocidadeAtual = velocidadeMaxima;
        System.out.println("Velocidade atual: " + velocidadeAtual + " km/h");
    }

    public void travar(int intensidade) {
        if (!ligado) {
            System.out.println("O carro está desligado! Não pode travar.");
            return;
        }
        velocidadeAtual -= intensidade;
        if (velocidadeAtual < 0)
            velocidadeAtual = 0;
        System.out.println("Velocidade atual: " + velocidadeAtual + " km/h");
    }

    public void buzinar() {
        System.out.println("Buzina padrão do carro.");
    }
}
