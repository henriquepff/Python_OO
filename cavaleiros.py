class Personagem:
    def __init__(self, nome, constelacao):
        self.nome = nome
        self.constelacao = constelacao

    def apresentar(self):
        print(f"\n{self.nome}, cavaleiro da constelação de {self.constelacao}.")


class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, poder_de_luta):
        super().__init__(nome, constelacao)
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        print(f"\n{self.nome} executa seu golpe especial com poder de luta {self.poder_de_luta}!")

class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casa_do_zoodiaco):
        super().__init__(nome, constelacao)
        self.casa_do_zoodiaco = casa_do_zoodiaco

    def defender_casa(self):
        print(f"\n{self.nome} defende a casa de {self.casa_do_zoodiaco} com honra!")


class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zoodiaco):
        CavaleiroDeOuro.__init__(self, nome, constelacao, casa_do_zoodiaco)
        self.poder_de_luta = poder_de_luta

    def golpe_especial(self):
        print(f"\n{self.nome} realiza um golpe híbrido com poder de luta {self.poder_de_luta}!")


    def defender_casa(self):
        print(f"\n{self.nome} protege a casa de {self.casa_do_zoodiaco} com poder total!")



def main():
    personagens = []

    while True:
        print("\n===MENU===")
        print("1. Cadastrar cavaleiro")
        print("2. Listar personagens")
        print("3. Executar habilidades")
        print("4. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nTipo de cavaleiro:")
            print("1. Cavaleiro de Bronze")
            print("2. Cavaleiro de Ouro")
            print("3. Cavaleiro Híbrido")
            tipo = input("Tipo: ")

            if tipo == "1":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                poder = input("Poder de luta: ")

                personagem = CavaleiroDeBronze(nome, constelacao, poder)

            elif tipo == "2":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                casa = input("Casa do zoodíaco: ")

                personagem = CavaleiroDeOuro(nome, constelacao, casa)
            
            elif tipo == "3":
                nome = input("\nNome: ")
                constelacao = input("Constelação: ")
                poder = input("Poder de luta: ")
                casa = input("Casa do zoodíaco: ")

                personagem = CavaleiroHibrido(nome, constelacao, poder, casa)

            else:
                print("\nTipo inválido!\n")
                continue

            
            personagens.append(personagem)
            print("\nCavaleiro cadastrado com sucesso.\n")

        elif opcao == "2":
           if not personagens:
               print("\nNenhum cavaleiro cadastrado.\n")
           else:
                print("\n---Cavaleiros---")
                for p in personagens:
                    p.apresentar()    

        elif opcao == "3":
            if not personagens:
               print("\nNenhum cavaleiro cadastrado.\n")
            else:
                print("\n---Habilidades---")
                for p in personagens:
                    print(f"\n{p.nome}: ")
                    if isinstance(p, CavaleiroDeBronze):
                        p.golpe_especial()
                    if isinstance(p, CavaleiroDeOuro):
                        p.defender_casa()
        

        elif opcao == "4":
            print("\nEncerrando o programa...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.")



if __name__ == "__main__":
    main()