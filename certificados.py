class Participante:
    def __init__(self, nome, email):
        self._nome = nome
        self._email = email

    def get_nome(self):
        return self._nome
    
    def get_email(self):
        return self._email

    def emitirCertificado(self):
        return f"{self._nome} - Certificado genérico de participação.\n"


class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.__curso = curso
    
    def get_curso(self):
        return self.__curso

    def emitirCertificado(self):
        return f"{self._nome} concluiu o curso de {self.__curso} com sucesso."


class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.__especialidade = especialidade
    
    def get_especialidade(self):
        return self.__especialidade

    def emitirCertificado(self):
        return f"{self.get_nome()} participopu como palestrante na área de {self.__especialidade}.\n"

def main():
    participantes = []

    while True:
        print("\n===MENU===")
        print("1. Cadastrar participante")
        print("2. Listar participantes")
        print("3. Emitir certificados")
        print("4. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nCadastrar:")
            print("1. Aluno")
            print("2. Instrutor")
            tipo = input("\nTipo de participante: ")

            if tipo == "1":
                nome = input("\nNome: ")
                email = input("Email: ")
                curso = input("Curso: ")
                participantes.append(Aluno(nome, email, curso))
                print("\nAluno cadastrado com sucesso.\n")
            elif tipo == "2":
                nome = input("\nNome: ")
                email = input("Email: ")
                especialidade = input("Especialidade: ")
                participantes.append(Instrutor(nome, email, especialidade))
                print("\nInstrutor cadastrado com sucesso.\n")
            else:
                print("Tipo inválido!")

        elif opcao == "2":
            if not participantes:
                print("\nNenhum participante cadastrado.\n")
            else:
                print("\n===Participantes Cadastrados===")
                for p in participantes:
                    if isinstance(p, Aluno):
                        print(f"Tipo: Aluno")
                        print(f"Nome: {p._nome}")
                        print(f"E-mail: {p._email}")
                        print(f"Curso: {p.get_curso()}\n")
                    else:
                        print(f"Tipo: Instrutor")
                        print(f"Nome: {p._nome}")
                        print(f"E-mail: {p._email}")
                        print(f"Especialidade: {p.get_especialidade()}\n")


        elif opcao == "3":
                 if not participantes:
                    print("\nNenhum participante cadastrado.\n")
                 else:
                    print("\n===Certificados===")
                    for p in participantes:
                        print(p.emitirCertificado())
        

        elif opcao == "4":
            print("\nEncerrando o programa...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.")



if __name__ == "__main__":
    main()