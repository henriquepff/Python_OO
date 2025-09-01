class ProgressaoAritmetica:
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def gerar_termos(self):
        termos = []
        for i in range(self.n):
            termo = self.a1 + self.r * i
            termos.append(termo)
        return termos

    def calcular_soma(self):
        an = self.a1 + self.r * (self.n - 1)
        soma = self.n * (self.a1 + an)/2
        return soma
    

def main():
    print("====Progressão Aritmética====")
    a1 = float(input("Digite o primeiro termo (a1): "))
    r = float(input("Digite a razão (r): "))
    n = int(input("Digite o número de termos (n): "))

    pa = ProgressaoAritmetica(a1,r,n)

    termos = pa.gerar_termos()

    print("\nTermos da P.A.: ")
    contador = 1
    for termo in termos:
        print(f"Termo {contador}: {termo}")
        contador += 1

    soma = pa.calcular_soma()

    print(f"\nSoma dos {n} termos: {soma}\n")





if __name__ == "__main__":
    main()