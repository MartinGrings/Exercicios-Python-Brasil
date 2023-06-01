class carro:
    def __init__(self, marca, motor, cor):
        self.marca = marca
        self.motor = motor
        self.cor = cor

    def mostrarMarca(self):
        return self.marca

    def mostrarMotor(self):
        return self.motor
    
    def mostrarCor(self):
        return self.cor
    
    

carro1 = carro("VW", "1.6","azul")

print(carro1.mostrarMarca())
print(carro1.mostrarMotor())
print(carro1.mostrarCor())

        