package Lab03.Ex02;

import Lab03.Aluno;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

public class AlunoSorterLambda {

    /**
     * Ordena a lista de Aluno com base no Comparator fornecido.
     *
     * @param alunos     A lista de Aluno a ser ordenada.
     * @param comparator O Comparator que define a ordem de sort.
     */
    public static void sort(List<Aluno> alunos, Comparator<Aluno> comparator) {
        if (alunos != null) {
            alunos.sort(comparator);
        }
    }

    /**
     * Imprime a lista de Aluno com uma mensagem de cabeçalho.
     *
     * @param message Mensagem de cabeçalho.
     * @param alunos  Lista de Aluno a ser impressa.
     */
    public static void printAlunos(String message, List<Aluno> alunos) {
        System.out.println("\n" + message);
        alunos.forEach(System.out::println);
    }

    /**
     * Ordena a lista de Aluno por nome lexicográfico.
     */
    public static void sortByNameLex(List<Aluno> alunos) {
        sort(alunos, Comparator.comparing(Aluno::getNome));
        printAlunos("Sort by Name (Lexicographical Order)", alunos);
    }

    /**
     * Ordena a lista de Aluno pelo tamanho do nome de forma crescente.
     */
    public static void sortByNameLength(List<Aluno> alunos) {
        sort(alunos, Comparator.comparingInt(a -> a.getNome().length()));
        printAlunos("Sort by Name Length", alunos);
    }

    /**
     * Ordena a lista de Aluno por nota de forma crescente.
     */
    public static void sortByNota(List<Aluno> alunos) {
        sort(alunos, Comparator.comparingInt(Aluno::getNota));
        printAlunos("Sort by Nota", alunos);
    }

    /**
     * Método principal para execução e testes.
     */
    public static void main(String[] args) {
        List<Aluno> alunos = Arrays.asList(
                new Aluno(1, "Ana-Maria", "Silva", 18),
                new Aluno(2, "João", "Carlos", 15),
                new Aluno(3, "Maria", "Santos", 12)
        );

        sortByNameLex(alunos);
        sortByNameLength(alunos);
        sortByNota(alunos);
    }
}
