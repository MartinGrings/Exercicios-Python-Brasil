class pessoa:
    def __init__(self,nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade +=1
        if self.idade < 21:
            self.altura += 0.5

    def engordar(self):
        self.peso += 1

    def emagrecer(self):
        self.peso -= 1

    def crescer(self):
        self.altura += 1 

    def __str__(self):
        return (f"Nome: {self.nome}\n" +
                f"Idade: {self.idade} anos\n" +
                f"Peso: {self.peso}Kg\n"+
                f"Altura: {self.altura}cm")


p1 = pessoa("Martin", 10, 40, 100)

print(p1)
print("-----------------------")
p1.envelhecer()
print(p1)
print("-----------------------")
p1.engordar()
print(p1)
print("-----------------------")
p1.crescer()
print(p1)
print("-----------------------")
p1.emagrecer()
print(p1)