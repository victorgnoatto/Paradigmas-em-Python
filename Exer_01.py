# Exercicio 01

# Num campeonato  europeu  de  volleyball,  se  inscreveram 30 países.
# Sabendo-se que na lista oficial de cada país consta, além de outros dados, peso e idade de 12 jogadores,
# criar um algoritmo que apresente as seguintes informações:

# a)o peso médio e a idade média de cada um dos times.
# b)o peso médio e a idade média de todos os participantes.

totpeso = 0
totid = 0
for i in range(1, 30):
 somapeso = 0
 somaid = 0
 for x in range(1, 12):
  peso = float(input('Digite o peso: '))
  id = int(input('Digite a idade: '))

  somapeso = somapeso + peso
  somaid = somaid + id

 print(f'Peso medio do time: {somapeso/12:.2f}')
 print(f'Idade media do time: {somaid/12:.2f}')
 totpeso = totpeso + somapeso
 totid = totid + somaid

print(f'Peso medio de todos os times: {totpeso/360:.2f}')
print(f'Idade media de todos os times:{totid /360:.2f}')

