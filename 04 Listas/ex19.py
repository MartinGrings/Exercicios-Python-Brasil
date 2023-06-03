print("""Qual o melhor Sistema Operacional para uso em servidores?

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro""")

dados = []

while True:
    valor = int(input("Digite sua resposta: "))
    while valor not in (range(0,7)):
        print("Respota inválida")
        valor = int(input("Digite sua resposta: "))
    if valor == 0:
        break
    else:
        dados.append(valor)

print()
print()
print()


print("""Sistema Operacional     Votos   %
-------------------     -----   ---""")

print(f"Windows Server           {dados.count(1)}      {round(((dados.count(1) / len(dados))*100),2)}%") # quantidade de valor / total -> * 100 -> arrendondado pra 2 casas decimais
print(f"Unix                     {dados.count(2)}      {round(((dados.count(2) / len(dados))*100),2)}%")
print(f"Linux                    {dados.count(3)}      {round(((dados.count(3) / len(dados))*100),2)}%")
print(f"Netware                  {dados.count(4)}      {round(((dados.count(4) / len(dados))*100),2)}%")
print(f"Mac OS                   {dados.count(5)}      {round(((dados.count(5) / len(dados))*100),2)}%")
print(f"Outro                    {dados.count(6)}      {round(((dados.count(6) / len(dados))*100),2)}%")

maior = dados.count(1)
numDoMaior = 1
for j in range(2,7):
    if dados.count(j) > maior:
        maior = dados.count(j)
        numDoMaior = j

nomes = {1:"Windows Server", 2:"Unix", 3:"Linux", 4:"Netware", 5:"MAC OS", 6:"Outro"}

print(f"""-------------------     -----
Total                    {len(dados)}
""")

print(f"O Sistema Operacional mais votado foi o {nomes[numDoMaior]}, com {maior} votos, correspondendo a {round(((maior / len(dados))*100),2)}% dos votos.")




