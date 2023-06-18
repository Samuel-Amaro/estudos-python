# UNSANDO MATEMATICA NO PYTHON, COM AUXILIO DA BIBLIOTECA MATH DA LINGUAGEM C, USANDO FUNÇÕES MATEMATICAS

import math # importando biblioteca

# numero PI
constantePi = math.pi
print('Numero de PI: {}'.format(constantePi))

# Funções teóricas dos números e de representação

# função que retorna o <= valor inteiro do paramentro passado
menorNumero = math.ceil(20) # retorna int
print('Menor Numero Inteiro >= 20 = {}'.format(menorNumero))

# função que retorna o fatorial de um numero inteiro passado por parametro
fatorial = math.factorial(3) # retorna int
print('Fatorial de 3 = {}'.format(fatorial))

# função que retorna o maior divisor comun entre dois valores inteiros diferentes de 0
mdc = math.gcd(100,10) # retorna int
print('maior numero que e divisor comun de {} e {}  = {}'.format(100,10,mdc))

# Retorne a raiz quadrada inteira do inteiro não negativo n . Este é o piso da raiz quadrada exata de n , ou equivalentemente o maior inteiro a tal que a ² ≤  n .

raizQuadrada = math.sqrt(100) # retorna float
print('Raiz quadrada de {} = {}'.format(100,raizQuadrada))

# Retorne as partes fracionárias e inteiras do valor informado
fracionario_inteiro = (math.modf(21.6)) # retorna um tupla = (float fracionario,float inteiro)
print('Parte Fracionaria e inteira do valor {} = {}'.format(21.6,fracionario_inteiro))

# Retorno x elevado a y (potenciação) ambos parametros diferentes de 0.
potenciacao = math.pow(10,2) # retorna um float
print('O valor {} elevado a {} = {}'.format(10,2,potenciacao)) 