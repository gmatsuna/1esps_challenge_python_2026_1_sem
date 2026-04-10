from pontos import CalcularPontos

class RegistrarDia:
    def __init__(self):
        self.passos = int(input("Passos: "))
        self.academia = input("Foi à academia? (s/n): ") == "s"
        self.alimentacao = input("Alimentação saudável? (s/n): ") == "s"
        self.hidratacao = input("Hidratou bem? (s/n): ") == "s"
        self.sono = input("Dormiu bem? (s/n): ") == "s"

    def somarPontos(self):
        calculadora = CalcularPontos()
        self.pontos = calculadora.somaDosPontos(self.passos, self.academia, self.alimentacao, self.hidratacao, self.sono)

        return self.pontos