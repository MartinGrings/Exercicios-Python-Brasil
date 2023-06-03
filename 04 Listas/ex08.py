idades = []
alturas = []

for j in range(0,5):
    idade = int(input(f"Digite a idade da pessoa {j+1}: "))
    idades.append(idade)
    altura = float(input(f"Digite a altura da pessoa {j+1}: "))
    alturas.append(altura)

print("----------------------------")

for k in range(4,-1,-1):
    print(f"Pessoa {k+1} idade: {idades[k]}, altura: {alturas[k]}")