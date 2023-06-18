# SIMULADOR DE LANÇAMENTO DE UM DADO

import random


resposta = 1
sequencia_salva = []

while resposta == 1:
        print("\n")
        print("-" * 38)
        # aleatorio gerado
        dado = random.randint(1,1000000)
        # salva sequencia gerada pelo usuario
        sequencia_salva.append(dado)
        try:
            resposta = int(input("ESCOLHA (1) PARA LANÇAR DADO (0) PARA SAIR: "))
            if resposta != 0 and resposta != 1:
                print("\n")
                print("-" * 38)
                print("DIGITE UMA RESPOSTA VALIDA.....|")
                print("-" * 38)
                resposta = 1
            elif resposta == 1:
                  print("\n")
                  print("-" * 3)
                  print(f"{dado} |")
                  print("-" * 3)
            elif resposta == 0 and resposta != 1:
                print("\n")
                print("-"*38)
                print("LANÇADOR DE DADO ENCERRADO.......|")
                print("-"*38)
                print("SEQUÊNCIA GERADA EM SUA UTILIZAÇÃO")
                for item in sequencia_salva:
                    print(f"{item} ", end='')
                print("\n")
                print("-"*38)    
        except TypeError as letra:
               print("\n")
               print("-" * 38)
               print("DIGITE UMA RESPOSTA VALIDA.....|")
               print("-" * 38) 
        except ValueError as letra:
               print("\n")
               print("-" * 38)
               print("DIGITE UMA RESPOSTA VALIDA....|")
               print("-" * 38) 