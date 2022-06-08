#Exercicio 03

# Faça  um  programa  que  faça  5  perguntas  para  uma  pessoa sobre um crime. As perguntas são:
# •"Telefonou para a vítima?"
# •"Esteve no local do crime?"
# •"Mora perto da vítima?"
# •“Tinha dívidas com a vítima?"
# •"Já trabalhou com a vítima?“
#
# O  programa  deve  no  final  emitir  uma  classificação  sobre  a  participação  da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
# "Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

lista_perguntas = ["Telefonou para a vítima? ( 1 )Sim ou ( 0 )Não: ",
"Esteve no local do crime? ( 1 )Sim ou ( 0 )Não: ",
"Mora perto da vítima? ( 1 )Sim ou ( 0 )Não: ",
"Devia para a vítima? ( 1 )Sim ou ( 0 )Não: ",
"Já trabalhou com a vítima? ( 1 )Sim ou ( 0 )Não: "]
res = []
soma_respostas = 0
for i in range(len(lista_perguntas)):
    print(lista_perguntas[i])
    res.append(input())
    soma_respostas += int(res[i])
status = ["Inocente", "Suspeita", "Cúmplice", "Cúmplice", "Assassino"]
if soma_respostas < 2:
    print(status[0])
else:
    print(status[soma_respostas-1])
