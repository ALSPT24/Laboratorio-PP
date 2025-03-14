package Lab02.Ex02;

import Lab01.Ex02.Condutor;

public class CarroReal extends CarroAbstrato implements Buzina {
    public CarroReal(String matricula, Condutor condutor) {
        super(matricula, condutor);
    }

    @Override
    public void buzinar() {
        System.out.println("Buzina do CarroReal: Toooooooot!");
    }
}
