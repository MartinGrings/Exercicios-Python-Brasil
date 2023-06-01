class retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudarLados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def retornarLados(self):
        return self.comprimento, self.largura
    
    def calcArea(self):
        return self.comprimento * self.largura

    def calcPerimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)
retangulo1 = retangulo(2,3)

print(retangulo1.retornarLados())
print(retangulo1.calcArea())
print(retangulo1.calcPerimetro())
retangulo1.mudarLados(4,5)
print(retangulo1.retornarLados())
print(retangulo1.calcArea())
print(retangulo1.calcPerimetro())
