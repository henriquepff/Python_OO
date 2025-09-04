class AnalisadorString:
    def __init__(self, texto):
        self.__texto = texto
    
    def numero_caracteres(self):
        return len(self.__texto)
    
    def maiusculas(self):
        return self.__texto.upper()
    
    def minusculas(self):
        return self.__texto.lower()
    
    def contar_vogais(self):
        vogais = 'aeiouAEIOU'
        contador = 0

        for caracter in self.__texto:
            if caracter in vogais:
                contador += 1
        
        return contador
    
    def contem_ifb(self):
        return "IFB" in self.__texto.upper()
    

def main():
    texto = input("\nDigite um texto: ")
    analisador = AnalisadorString(texto)

    print("\n===Análise do Texto===\n")
    print(f"Número de caracteres: {analisador.numero_caracteres()}")
    print(f"Em maiúsculas: {analisador.maiusculas()}")
    print(f"Em minúsculas: {analisador.minusculas()}")
    print(f"Número de vogais: {analisador.contar_vogais()}")

    if analisador.contem_ifb():
        print("A substring 'IFB' aparece no texto (independente de maiúsculas ou minúsculas).\n")
    else:
        print("A substring 'IFB' NÃO aparece no texto.\n")


if __name__ == "__main__":
    main()