import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Biblioteca {
    private List<List<String>> livros;
    private List<String> novoLivro;

    public Biblioteca() {
        this.livros = new ArrayList<>();
        this.novoLivro = new ArrayList<>();
    }

    public void adicionarLivro(String titulo, String anoLancamento, String autor, String genero) {
        List<String> novoLivro = new ArrayList<>();
        novoLivro.add(titulo);
        novoLivro.add(anoLancamento);
        novoLivro.add(autor);
        novoLivro.add(genero);
        livros.add(novoLivro);
    }

    public boolean verificaTitulo(String titulo) {
        for (List<String> l : livros) {
            if (l.get(0).equals(titulo)) {
                System.out.println();
                System.out.println("Titulo ja disponivel na biblioteca");
                return true;
            }
        }
        return false;
    }

    public void consultarPorTitulo(String titulo) {
        System.out.println();
        boolean encontrou = false;
        for (List<String> l : livros) {
            if (!l.isEmpty() && l.get(0).toLowerCase().contains(titulo.toLowerCase())) {
                System.out.println("Titulo: " + l.get(0));
                System.out.println("Ano de lancamento: " + l.get(1));
                System.out.println("Autor: " + l.get(2));
                System.out.println("Genero: " + l.get(3));
                System.out.println();
                encontrou = true;
            }
        }
        if (!encontrou) {
            System.out.println("Titulo nao encontrado.");
        }
        System.out.println();
    }

    public void consultarPorGenero(String genero) {
        System.out.println();
        boolean encontrou = false;
        for (List<String> l : livros) {
            if (!l.isEmpty() && l.get(3).toLowerCase().contains(genero.toLowerCase())) {
                System.out.println("Titulo: " + l.get(0));
                System.out.println("Ano de lancamento: " + l.get(1));
                System.out.println("Autor: " + l.get(2));
                System.out.println("Genero: " + l.get(3));
                System.out.println();
                encontrou = true;
            }
        }
        if (!encontrou) {
            System.out.println("Genero nao encontrado.");
        }
        System.out.println();
    }

    public boolean adicionarLivroParaLeitura(String titulo) {
        if(novoLivro.size() < 3) {
            for (String t : novoLivro) {
                if (t.equalsIgnoreCase(titulo)) {
                    System.out.println();
                    System.out.println("Titulo ja encontrado na lista para leitura.");
                    return false;
                }
            }
            novoLivro.add(titulo);
            return true;
        } else {
            System.out.println();
            System.out.println("Limite atingido de livros adicionados para leitura.");
            return false;
        }
        
    }

    public boolean removerLivroParaLeitura(String titulo) {
        for (String t : novoLivro) {
            if (t.equalsIgnoreCase(titulo)) {
                novoLivro.remove(t);
                return true;
            }
        }
        return false;
    }

    public void mostrarLivrosParaLeitura() {
        System.out.println();
        if (!novoLivro.isEmpty()) {
            for (int i = 0; i < novoLivro.size(); i++) {
                System.out.println((i + 1) + ". " + novoLivro.get(i));
            }
            System.out.println();
        } else {  
            System.out.println("Lista de leitura vazia.");
        }
        System.out.println();
    }

    public boolean verificaAno(String ano) {
        try {
            int anoInt = Integer.parseInt(ano);
            if (anoInt < 1900 || anoInt > 2024) {
                System.out.println();
                System.out.println("Ano fora do intervalo.");
                System.out.println();
                return false;
            }
            return true;
        } catch (NumberFormatException e) {
            System.out.println();
            System.out.println("Tipo de dado invalido para ano.");
            System.out.println();
            return false;
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Biblioteca biblioteca = new Biblioteca();

        while (true) {
            System.out.println("1. Adicionar livro");
            System.out.println("2. Consultar por titulo");
            System.out.println("3. Consultar por genero");
            System.out.println("4. Adicionar livros para leitura");
            System.out.println("5. Remover livros para leitura");
            System.out.println("6. Mostrar livros para leitura");
            System.out.println("7. Sair");
            System.out.print(">>> ");
            String menu = scanner.nextLine();

            if (menu.equals("1")) {
                System.out.print("Titulo: ");
                String titulo = scanner.nextLine();
                boolean tituloRepetido = biblioteca.verificaTitulo(titulo);
                if (tituloRepetido) {
                    continue;
                }
                System.out.print("Ano: ");
                String ano = scanner.nextLine();
                boolean sucesso = biblioteca.verificaAno(ano);
                if (!sucesso) {
                    continue;
                }
                System.out.print("Autor: ");
                String autor = scanner.nextLine();
                System.out.print("Genero: ");
                String genero = scanner.nextLine();
                biblioteca.adicionarLivro(titulo, ano, autor, genero);
                System.out.println();
                System.out.println("Livro adicionado com sucesso!");
                System.out.println();

            } else if (menu.equals("2")) {
                System.out.print("Digite o titulo: ");
                String titulo = scanner.nextLine();
                biblioteca.consultarPorTitulo(titulo);

            } else if (menu.equals("3")) {
                System.out.print("Digite o genero: ");
                String genero = scanner.nextLine();
                biblioteca.consultarPorGenero(genero);

            } else if (menu.equals("4")) {
                System.out.print("Digite o titulo: ");
                String titulo = scanner.nextLine();
                boolean sucesso = biblioteca.adicionarLivroParaLeitura(titulo);
                System.out.println();
                if (sucesso) {
                    System.out.println("Titulo adicionado!");
                } else {
                    System.out.println("Nao foi possivel adicionar o livro.");
                }
                System.out.println();

            } else if (menu.equals("5")) {
                System.out.println();
                System.out.print("Digite o titulo: ");
                String titulo = scanner.nextLine();
                boolean sucesso = biblioteca.removerLivroParaLeitura(titulo);
                if (sucesso) {
                    System.out.println("Titulo removido com sucesso!");
                } else {
                    System.out.println("Titulo nao encontrado para remocao.");
                }
                System.out.println();

            } else if (menu.equals("6")) {
                biblioteca.mostrarLivrosParaLeitura();

            } else if (menu.equals("7")) {
                break;
            }
        }
        scanner.close();
    }
}
