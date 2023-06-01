numeros = []

for j in range(0,5):
    num = int(input("Digite um número: "))
    numeros.append(num)

soma = 0

for i in numeros:
    soma += i

multiplicacao = numeros[0]

for k in range(1,len(numeros)):
    multiplicacao = multiplicacao * numeros[k]
    
numerosString = f"{numeros[0]}"
for l in range(1,len(numeros)):
    numerosString += f", {numeros[l]}"

print(f"Os número digitados foram: {numerosString}")
print(f"Soma dos números: {soma}")
print(f"Multiplicação do número: {multiplicacao}")