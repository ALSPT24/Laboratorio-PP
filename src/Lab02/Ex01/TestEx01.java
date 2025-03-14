package Lab02.Ex01;

import Lab01.Ex02.*;
import java.util.ArrayList;
import java.util.List;

public class TestEx01 {
    public static void main(String[] args) {
        Condutor condutor1 = new Condutor("João", 30, 5);
        Condutor condutor2 = new Condutor("Maria", 25, 6);
        Condutor condutor3 = new Condutor("Carlos", 40, 7);

        Carro citadino1 = new Citadino("AAA-1111", condutor1);
        Carro citadino2 = new Citadino("BBB-2222", condutor2);
        Carro citadino3 = new Citadino("CCC-3333", condutor3);

        List<Carro> carros = new ArrayList<>();
        carros.add(citadino1);
        carros.add(citadino2);
        carros.add(citadino3);

        for (Carro carro : carros) {
            carro.ligar();
            carro.acelerar();
            carro.buzinar();

            if (carro instanceof Citadino) {
                System.out.println("---- Using the element of the list as Citadino ----");
                ((Citadino) carro).ligarACManual();
            }

            carro.desligar();
            System.out.println("---------------------------------------");
        }
    }
}