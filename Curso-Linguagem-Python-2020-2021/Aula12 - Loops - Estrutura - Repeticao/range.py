# função range()

 # permite gerar sequencia de valores
  # valores em progressão aritmetica
  # muito util para gerar as listas de valores para o comando for

  # formas de uso

  # range(N) : gera valores inteiros de 0 até N-1
  # N - valor final
  # range(M,N) : gera valores inteiros de M até N-1
  # M - valor inicial | N - valor final
  # range(M,N,D) : gera os valores inteiros M,M + D, M +2D,... inferios a N
  # M - valor inicial
  # N - valor final
  # D - de quanto em quanto o incremento

# gera valores 0,1,2,3,4
for x in range(5):
      print("Valor = ",x)

# gera valores 0,1,2,3,4,5,6,7,8,9
for x in range(10):
    print("Valor = ",x)         

# gera valores 3,4,5,6,7,8,9
for x in range(3,10):
      print("Valor = ",x)

# gera valores 3,5,7,9
for x in range(3,10,2):
      print("Valor = ",x)          