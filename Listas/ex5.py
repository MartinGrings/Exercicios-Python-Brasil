
todos = []
par = []
impar = []

for j in range(0,5):
    num = int(input("Digite um número inteiro: ")) 
    todos.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(todos)
print(par)
print(impar)

