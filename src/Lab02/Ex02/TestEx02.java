package Lab02.Ex02;

import Lab01.Ex02.Condutor;

public class TestEx02 {
    public static void main(String[] args) {
        // Criar um objeto Condutor
        Condutor condutor = new Condutor("Bob", 35, 7);

        // Criar um objeto CarroReal
        CarroReal carro = new CarroReal("DDD-4444", condutor);

        // Interações com o objeto CarroReal
        carro.ligar();
        carro.acelerar();
        carro.buzinar();
        carro.travar(15);
        carro.desligar();
    }
}