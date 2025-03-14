package Lab02.Ex02;

import Lab01.Ex02.*;

public abstract class CarroAbstrato extends Carro {
    public CarroAbstrato(String matricula, Condutor condutor) {
        super(matricula, condutor);
    }

    public abstract void buzinar();
}
