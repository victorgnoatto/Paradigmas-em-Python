#Exercicio 04

#Suponha  um  dicionário  D  de  estudantes,  como  definida  no exemplo abaixo, onde cada par consiste
# de nome do estudante e das notas do mesmo. Escreva uma função chamada “aprovados” que receba como entrada o
# dicionário D e imprima o nome dos alunos aprovados. Um aluno é aprovado quando todas as suas notas são maiores que 7.
# Por exemplo,aprovados(D) deverá imprimir
# Denise. D={'Alano':(7.5,8.0,6.5),'Denise':(9.0,8.5,9.5),'Ana Paula':(3.5,1.0,6.5)}

N = int(input('Quantos alunos? '))

estudantes = {}

for i in range(1, N+1):
  name = input(f'Nome do aluno {i}: ')
  grades = []

  for j in range(1, 5):
    grade = float(input(f'Nota {j} do aluno {i}: '))
    grades.append(grade)

  estudantes[name] = grades

for name, grades in estudantes.items():
  media = sum(grades) / len(grades)
  result = 'aprovado' if media >= 7.0 else 'reprovado'
  print(f'O aluno {name} foi {result} com média {media:.1f}')