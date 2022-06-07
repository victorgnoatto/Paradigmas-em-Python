# Exercicio  02

# Criar  um  algoritmo  que  entre  com  vários  números  inteiros positivos e
# imprima o produto dos números ímpares digitados e a soma dos pares.

soma = 0
prod = 1

num = int(input('Digite um numero positivo ou digite 0 (zero) para terminar: '))
while num > 0:
    if num % 2 == 0:
        soma = soma + num

    else:
        prod = prod * num
    num = int(input('Digite outro numero ou digite 0 (zero) para terminar : '))

print(f'Produto dos numeros impares: {prod}')
print(f'Soma dos numeros pares: {soma}')

