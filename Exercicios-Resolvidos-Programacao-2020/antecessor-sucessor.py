# obtenha um valor do usuario e mostre, o ancetessor e sucessor desse valor
valor = int(input('Digite um valor: '))

antecessor = valor - 1
print('Antecessor de {} e {}'.format(valor,antecessor))
sucessor = valor + 1
print('Sucessor de {} e {}'.format(valor,sucessor))