class Livro:
    def __init__(self, titulo, autor, id_livro):
        self.__titulo = titulo
        self.__autor = autor
        self.__id_livro = id_livro

    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor
    
    def get_id_livro(self):
        return self.__id_livro
    
    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    def set_autor(self, novo_autor):
        self.__autor = novo_autor

    def set_id_livro(self, novo_id):
        self.__id_livro = novo_id


class Usuario:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__livros_emprestados = []

    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula

    def emprestar_livros(self, livro):
        self.__livros_emprestados.append(livro)
        print(f"{self.__nome} pegou emprestado o livro '{livro.get_titulo()}'.")

    def devolver_livro(self, id_livro):
        for livro in self.__livros_emprestados:
            if livro.get_id_livro() == id_livro:
                self.__livros_emprestados.remove(livro)
                print(f"\n{self.__nome} devolveu o livro '{livro.get_titulo()}'.\n")
                return
            
        print(f"\n{self.__nome} não possui um livro com ID {id_livro}.\n")

    def listar_livros_emprestados(self):
        if not self.__livros_emprestados:
            print("\nNenhum livro emprestado.\n")
        else:
            print("\nLivros emprestados: ")
            for livro in self.__livros_emprestados:
                print(f"- {livro.get_titulo()} ({livro.get_id_livro()})")

    
def main():
    livro1 = Livro("Harry Potter", "J. K. Rolling", 1)
    livro2 = Livro("Jogos Vorazes", "Susan Colling", 2)
    livro3 = Livro("Dom Casmurro", "Machado de Assis", 3)

    usuario1 = Usuario("Marcos", 659875)

    usuario1.emprestar_livros(livro1)
    usuario1.emprestar_livros(livro2)

    usuario1.listar_livros_emprestados()

    usuario1.devolver_livro(2)

    usuario1.listar_livros_emprestados()



if __name__ == "__main__":
    main()