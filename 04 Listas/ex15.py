notas = []

while True:
    nota = float(input("Digite a nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)

print(f"Quantidade de notas: {(len(notas))}") #a

ordemInformados = f"{notas[0]}"

for k in range(1,len(notas)):
    ordemInformados += f", {notas[k]}"

print(f"Ordem que os números foram informados: {ordemInformados}") #b

print("Ordem inversa à que os números foram informados: ")
for j in range(-1,(-len(notas)-1), -1):
    print(notas[j])                                             #c

soma = 0
for nota in notas:
    soma += nota

print(f"A soma dos valores é : {soma}") #d
media = soma/len(notas)
print(f"A média dos valores é: {media}") #e

acimaMedia = []
abaixoSete = []

for nota in notas:
    if nota > (media):
        acimaMedia.append(nota)
    elif nota < 7:
        abaixoSete.append(nota)

try:
    acimaMediaString = acimaMedia[0]
except IndexError:
    acimaMediaString = ""

for j in range(1, len(acimaMedia)):
      acimaMediaString += f", {acimaMedia[j]}"

print(f"Existem {len(acimaMedia)} valores acima da média calculada, que são: {acimaMediaString}") #f

acimaSeteString = str(abaixoSete[0])

for k in range(1,len(abaixoSete)):
    acimaSeteString += f", {(abaixoSete[k])}"

print(f"Existem {len(abaixoSete)} valores abaixo de sete, que são: {acimaSeteString}")

