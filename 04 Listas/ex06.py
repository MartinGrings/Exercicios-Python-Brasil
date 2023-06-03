mediaNotas = []

for j in range (0,3):
    notasAluno = [] 
    total = 0
    for i in range(0,4):
        nota = float(input(f"Digite a nota do aluno {j+1}: "))
        while nota < 0 or nota > 10:
            print("Nota inválida")
            nota = float(input(f"Digite a nota do aluno {j+1}: "))
        notasAluno.append(nota)
    
    for k in range(0,len(notasAluno)):
        total += notasAluno[k]        
    mediaNotas.append(total/4)
    print("--------------------")

print(mediaNotas)
passaram = 0
for l in range(0,len(mediaNotas)):
    if mediaNotas[l] >= 7:
        passaram += 1 
print(f"{passaram} alunos tem nota igual ou maior que sete")