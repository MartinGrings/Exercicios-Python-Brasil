class quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self,lado):
        self.lado = lado
    
    def mostrarValorLado (self):
        return (self.lado)
    
    def calcArea(self):
        return (self.lado * self.lado)
    

quadrado1 = quadrado(2)

print(quadrado1.mostrarValorLado())
print(quadrado1.calcArea())
quadrado1.mudarLado(3)
print(quadrado1.mostrarValorLado())
print(quadrado1.calcArea())
        