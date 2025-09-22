class Personagem:
    def __init__(self, nome, nivel):
        self._nome = nome
        self._nivel = nivel

    
    def atacar(self):
        print(f"\n{self._nome} realiza um ataque genérico.")


class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.__forca = forca
    
    def atacar(self):
        print(f"\n{self._nome} realiza um ataque físico! (Força: {self.__forca}).")


class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.__mana = mana
    
    def atacar(self):
        print(f"\n{self._nome} realiza um ataque mágico! (Mana: {self.__mana}).")


def main():
    personagem = Personagem("Ragna", 7)
    guerreiro = Guerreiro("Krastus", 8, 81)
    mago = Mago("Nextage", 9, 95)

    lista_personagens = [personagem, guerreiro, mago]

    print("\n---Ação dos Personagens---")
    for p in lista_personagens:
        p.atacar()




if __name__ == "__main__":
    main()