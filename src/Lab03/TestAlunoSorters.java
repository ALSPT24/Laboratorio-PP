package Lab03;

import Lab03.Ex01.AlunoSorterBubble;
import Lab03.Ex02.AlunoSorterLambda;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

public class TestAlunoSorters {

    private List<Aluno> originalAlunos;

    @BeforeEach
    void setUp() {
        originalAlunos = new ArrayList<>(Arrays.asList(
                new Aluno(1, "Ana-Maria", "Silva", 18),
                new Aluno(2, "João", "Carlos", 15),
                new Aluno(3, "Maria", "Santos", 12)
        ));
    }

    private List<Aluno> getFreshAlunos() {
        List<Aluno> freshList = new ArrayList<>();
        for (Aluno aluno : originalAlunos) {
            freshList.add(new Aluno(aluno.getId(), aluno.getNome(), aluno.getApelido(), aluno.getNota()));
        }
        return freshList;
    }

    @Test
    void testSortByNameLex() {
        List<Aluno> alunos = getFreshAlunos();
        AlunoSorterLambda.sortByNameLex(alunos);
        assertEquals("Ana-Maria", alunos.get(0).getNome());
        assertEquals("João", alunos.get(1).getNome());
        assertEquals("Maria", alunos.get(2).getNome());
    }

    @Test
    void testBubbleSortByNameLength() {
        List<Aluno> alunos = getFreshAlunos();
        AlunoSorterBubble.bubbleSortPorTamanhoNome(alunos);
        assertEquals("João", alunos.get(0).getNome());
        assertEquals("Maria", alunos.get(1).getNome());
        assertEquals("Ana-Maria", alunos.get(2).getNome());
    }

    @Test
    void testSortByNota() {
        List<Aluno> alunos = getFreshAlunos();
        AlunoSorterLambda.sortByNota(alunos);
        assertEquals(12, alunos.get(0).getNota());
        assertEquals(15, alunos.get(1).getNota());
        assertEquals(18, alunos.get(2).getNota());
    }

    @Test
    void testBubbleSortByNota() {
        List<Aluno> alunos = getFreshAlunos();
        AlunoSorterBubble.bubbleSortPorNota(alunos);
        assertEquals(12, alunos.get(0).getNota());
        assertEquals(15, alunos.get(1).getNota());
        assertEquals(18, alunos.get(2).getNota());
    }

    @Test
    void testSortEmptyList() {
        List<Aluno> emptyList = new ArrayList<>();
        AlunoSorterLambda.sortByNameLex(emptyList);
        assertTrue(emptyList.isEmpty());
    }

    @Test
    void testBubbleSortSingleElement() {
        List<Aluno> singleAluno = new ArrayList<>(Arrays.asList(
                new Aluno(1, "Ana-Maria", "Silva", 18)
        ));
        AlunoSorterBubble.bubbleSortPorNota(singleAluno);
        assertEquals(1, singleAluno.size());
        assertEquals("Ana-Maria", singleAluno.get(0).getNome());
    }
}