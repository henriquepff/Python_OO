class Documento:
    def __init__(self, titulo, conteudo):
        self.__titulo = titulo
        self.__conteudo = conteudo

    def get_titulo(self):
        return self.__titulo
    
    def get_conteudo(self):
        return self.__conteudo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_conteudo(self, conteudo):
        self.__conteudo = conteudo


class Impressora:
    def imprimir(self, documento):
        print("\n===Impressão do Documento===")
        print(f"Título: {documento.get_titulo()}")
        print(f"Conteúdo: {documento.get_conteudo()}")
        print("=================================")
        

def main():
    documentos = []
    impressora = Impressora()

    while True:
        print("\n====MENU====")
        print("1. Criar novo documento")
        print("2. Listar documentos")
        print("3. Imprimir documento")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            titulo = input("\nDigite o título do documento: ")
            conteudo = input("Digite o conteúdo do documento: ")
            doc = Documento(titulo, conteudo)
            documentos.append(doc)
            print("\nDocumento criado com sucesso!\n")
        
        elif opcao == "2":
            if not documentos:
                print("\nNenhum documento criado ainda.\n")
            else:
                print("\n===Lista de Documentos===")
                for i, doc in enumerate(documentos):
                    print(f"{i + 1}. {doc.get_titulo()}")
        
        elif opcao == "3":
            if not documentos:
                print("\nNenhum documento disponível para impressão.\n")
            else:
                print("\nEscolha o número do documento para imprimir: ")
                for i, doc in enumerate(documentos):
                    print(f"{i + 1}. {doc.get_titulo()}")

                escolha = input("\nNúmero: ")
                if escolha.isdigit():
                    escolha = int(escolha)
                    if 1 <= escolha <= len(documentos):
                        impressora.imprimir(documentos[escolha - 1])
                    else:
                        print("\nNúmero inválido.\n")
                else:
                    print("\nEntrada inválida.Digite um número.\n")

        elif opcao == "4":
            print("\nEncerrando o programa...\n")
            break

        else:
            print("\nOpção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()