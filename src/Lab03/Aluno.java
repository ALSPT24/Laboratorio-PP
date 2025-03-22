package Lab03;

public class Aluno {
    private int id;
    private String nome;
    private String apelido;
    private int nota;

    public Aluno(int id, String nome, String apelido, int nota) {
        this.id = id;
        this.nome = nome;
        this.apelido = apelido;
        this.nota = nota;
    }

    public int getId() { return id; }
    public String getNome() { return nome; }
    public String getApelido() { return apelido; }
    public int getNota() { return nota; }

    public void setId(int id) { this.id = id; }
    public void setNome(String nome) { this.nome = nome; }
    public void setApelido(String apelido) { this.apelido = apelido; }
    public void setNota(int nota) { this.nota = nota; }

    @Override
    public String toString() {
        return nome + " " + apelido + " (" + nota + ")";
    }
}