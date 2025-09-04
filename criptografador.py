
class Criptografador:
    def __init__(self,frase):
        self.__frase = frase
    
    def criptografar(self):
        substituicoes = {
            'a':'4','A':'4',
            'e':'3','E':'3',
            'i':'1','I':'1',
            'o':'0','O':'0',
            'u':'8','U':'8'
        }

        frase_criptografada = ""
        for caracter in self.__frase:
            if caracter in substituicoes:
                frase_criptografada += substituicoes[caracter]
            else:
                frase_criptografada += caracter
            
        return frase_criptografada


def main():
    frase = input("\nDigite uma frase para criptografar: ")
    criptografador = Criptografador(frase)

    resultado = criptografador.criptografar()

    print("\nFrase criptografada:")
    print(resultado + "\n")



if __name__ == "__main__":
    main()