numeros = []

for j in range (0,3):
    num = int(input(f"Digite o {j+1}º número: "))
    numeros.append(num)

somaDosQuadrados = 0

for numero in numeros:
    somaDosQuadrados += numero * numero

print(f"A soma dos quadrados do número é {somaDosQuadrados}")

