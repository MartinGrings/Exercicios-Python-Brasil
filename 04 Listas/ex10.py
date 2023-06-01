lista1 = []
lista2 = []

for k in range(0,5):
    valor = input("Digite um valor para a lista 1: ")
    lista1.append(valor)

for j in range(0,5):
    valor = input("Digite um valor para a lista 2: ")
    lista2.append(valor)

listaIntercalada = []

for l in range(0,len(lista1)):
    listaIntercalada.append(lista1[l])
    listaIntercalada.append(lista2[l])


print(listaIntercalada)
