package Lab02.Ex01;

import Lab01.Ex02.*;

import java.util.ArrayList;
import java.util.List;

class Van extends Carro {
    public Van(String matricula, Condutor conductor) {
        super(matricula, conductor);
    }

    public void desligarAirbagPassageiro() {
        System.out.println("Airbag desligado!");
    }

    @Override
    public void buzinar() {
        System.out.println("Buzina do Van: Bip Bip");
    }
}