#Exercicio 05

# Crie  um  dicionário  que  é  uma  agenda  e  coloque  nele  os seguintes  dados:
# chave,  nome,  idade,  telefone.  O  programa  deve  ler  um número indeterminado de dados,
# criar a agenda e imprimir todos os itens do dicionário no formato chave: nome-idade-fone.

dados = {}
cadastro = 's'
while cadastro == 's':
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    telefone = input('Digite seu telefone: ')
    dados[nome] = [nome, idade, telefone]
    cadastro = input('Deseja adicionar outra pessoa no cadastro? (s/n)').lower()
print(dados)