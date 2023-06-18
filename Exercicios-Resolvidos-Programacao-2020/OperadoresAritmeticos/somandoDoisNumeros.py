# CRIE UM PROGRAMA QUE SOME DOIS NUMEROS E MOSTRE O RESULTADO DA SOMA ENTRE ELES

# PARA LER UM VALOR NUMERICO DO TECLADO TEM QUE FAZER UM CAST NO INPUT, PARA PODER TER O VALOR CERTO

valor01 = int(input('Digite Um Valor: '))
valor02 = int(input('Digite Outro Valor: '))

resultadoSoma = valor01 + valor02

print("A soma entre {}".format(valor01) + " + {}".format(valor02) + " = {}".format(resultadoSoma))