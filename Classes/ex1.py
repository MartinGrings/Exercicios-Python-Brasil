class bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self,corNova): 
        self.cor = corNova

    def mostraCor(self):
        print(self.cor)
    

bola1 = bola("verde", 123, "plastico")
print(bola1.cor)
print(bola1.circunferencia)
print(bola1.material)

bola1.trocaCor("abc")
bola1.mostraCor()
