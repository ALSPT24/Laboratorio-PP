package Lab02.Ex01;

import Lab01.Ex02.*;

import java.util.ArrayList;
import java.util.List;

public class Citadino extends Carro {
    public Citadino(String matricula, Condutor conductor) {
        super(matricula, conductor);
    }

    public void ligarACManual() {
        System.out.println("AC ligado!");
    }

    @Override
    public void buzinar() {
        System.out.println("Buzina do Citadino: Piii Piii!");
    }
}
