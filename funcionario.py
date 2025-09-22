class Funcionario:
    def __init__(self, nome, salarioBase):
        self._nome = nome
        self._salarioBase = salarioBase

    
    def calcularSalario(self):
        return self._salarioBase
    

    def exibirDados(self):
        print(f"\nNome: {self._nome}")
        print(f"Salário: R$ {self.calcularSalario():.2f}")

class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, salarioBase, comissao):
        super().__init__(nome, salarioBase)
        self.__comissao = comissao

    def calcularSalario(self):
        return self._salarioBase + self.__comissao
    
    def exibirDados(self):
        print(f"\nNome: {self._nome}")
        print(f"Salário Base: R$ {self._salarioBase:.2f}")
        print(f"Comissão: R$ {self.__comissao:.2f}")
        print(f"Salário Total: R$ {self.calcularSalario():.2f}\n")

def main():
    func1 = Funcionario("Maria",3000.0)
    func2 = FuncionarioComissionado("João", 2500.0, 800.0)

    func1.exibirDados()
    print("--------------")
    func2.exibirDados()




if __name__ == "__main__":
    main()