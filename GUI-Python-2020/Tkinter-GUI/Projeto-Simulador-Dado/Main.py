import random

try:
        print("Você gostaria de jogar o dado ?")
        resposta = input("S - sim | N - nao: ")
        while(resposta == 'S' or resposta != 'N'):
              if(resposta == 'S'):
                #gera numero aleatorio entre 0 e 6
                aleatorio = random.randrange(0,6)  
                print(f"Caiu no numero: {aleatorio}")
                print("Você gostaria de jogar o dado ?")
                resposta = input("S - sim | N - nao: ")
              else:
                print("Opção invalida")  
                print("Você gostaria de jogar o dado ?")
                resposta = input("S - sim | N - nao: ")    
                    
except ValueError as identifier:
        print("A resposta deve ser de tipo caracter" + identifier)


 