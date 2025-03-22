package Lab03.Ex01;

import Lab03.Aluno;
import java.util.Collections;
import java.util.List;

public class AlunoSorterBubble {
    /**
     * Ordena a lista de alunos por nome de forma lexicográfica usando Bubble Sort.
     *
     * @param alunos A lista de Aluno a ser ordenada.
     */
    public static void bubbleSortPorNomeLex(List<Aluno> alunos) {
        if (alunos == null || alunos.isEmpty()) return;

        for (int i = 0; i < alunos.size() - 1; i++) {
            for (int j = 0; j < alunos.size() - 1 - i; j++) {
                if (alunos.get(j).getNome().compareTo(alunos.get(j + 1).getNome()) > 0) {
                    Collections.swap(alunos, j, j + 1);
                }
            }
        }
    }

    /**
     * Ordena a lista de alunos pelo tamanho do nome de forma crescente usando Bubble Sort.
     *
     * @param alunos A lista de Aluno a ser ordenada.
     */
    public static void bubbleSortPorTamanhoNome(List<Aluno> alunos) {
        if (alunos == null || alunos.isEmpty()) return;

        for (int i = 0; i < alunos.size() - 1; i++) {
            for (int j = 0; j < alunos.size() - 1 - i; j++) {
                if (alunos.get(j).getNome().length() > alunos.get(j + 1).getNome().length()) {
                    Collections.swap(alunos, j, j + 1);
                }
            }
        }
    }

    /**
     * Ordena a lista de alunos por nota de forma crescente usando Bubble Sort.
     *
     * @param alunos A lista de Aluno a ser ordenada.
     */
    public static void bubbleSortPorNota(List<Aluno> alunos) {
        if (alunos == null || alunos.isEmpty()) return;

        for (int i = 0; i < alunos.size() - 1; i++) {
            for (int j = 0; j < alunos.size() - 1 - i; j++) {
                if (alunos.get(j).getNota() > alunos.get(j + 1).getNota()) {
                    Collections.swap(alunos, j, j + 1);
                }
            }
        }
    }
}