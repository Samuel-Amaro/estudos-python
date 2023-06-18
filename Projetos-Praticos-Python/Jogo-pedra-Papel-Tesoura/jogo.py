"""
  # JOGO DE PEDRA PAPEL E TESOURA ENTRE USUARIO E MAQUINA

    - O objetivo é criar um jogo de linha de comando onde um usuário tem a chance de escolher entre pedra, papel e tesoura e se o usuário ganhar a pontuação é adicionada e, no final, quando o usuário termina o jogo, a pontuação é mostrada para o usuário.

    -  Faça a escolha do usuário e, em seguida, compare-a com a escolha do computador que é feita usando o módulo aleatório de uma lista de opções e, se o usuário vencer, aumente a pontuação em 1.
"""

import random


opcao_jogador = ''; opcao_maquina = ''; pontuacao_jogador = 0; pontuacao_maquina = 0; opcoes_jogo = ["PEDRA","PAPEL","TESOURA"]
controle_partida = True


while (pontuacao_maquina > pontuacao_jogador and pontuacao_maquina < 3) or (pontuacao_jogador > pontuacao_maquina and pontuacao_jogador < 3):

    print("#" * 40)
    print("       REGRAS DO JOGO        ")
    print("1 - QUEM FIZER TRÊS PONTOS PRIMEIRO GANHA!")
    print("2 - OPÇÕES INVALIDAS SERÃO ANULADAS, MAS NÃO ANULA PARTIDA!")
    print("3 - SEJA INTELIGENTE A MAQUINA NÃO VAI FACILITAR!")
    print("#" * 40)

    opcao_jogador = input("ESCOLHA SUA OPÇÃO: [PEDRA] [PAPEL] [TESOURA]: ")

    if(opcao_jogador in opcoes_jogo):
        jogada_maquina = random.randint(0,2)
        if(opcao_jogador == opcoes_jogo[jogada_maquina]):
            print("-" * 40) 
            print("OCORREU EMPATE ENTRE OS DOIS")
            print("-" * 40)
            pontuacao_maquina += 1
            pontuacao_jogador += 1
    
    elif(opcao_jogador == "PEDRA"):
        if(opcoes_jogo[jogada_maquina] == "PAPEL"):
           print("-" * 40) 
           print(f"VOCÊ PERDEU! CPU: {opcoes_jogo[jogada_maquina]} COBRE VOCÊ: {opcao_jogador}")
           print("-" * 40)           
           pontuacao_maquina += 1
        else:
            print("-" * 40) 
            print(f"VOCÊ GANHOU! VOCÊ: {opcao_jogador} ESMAGA CPU: {opcoes_jogo[jogada_maquina]}  ")
            print("-" * 40)
            pontuacao_jogador += 1 
    
    elif(opcao_jogador == "TESOURA"):
        if(opcoes_jogo[jogada_maquina] == "PEDRA"):
           print("-" * 40) 
           print(f"VOCÊ PERDEU! CPU: {opcoes_jogo[jogada_maquina]} ESMAGA VOCÊ: {opcao_jogador}")
           print("-" * 40)
           pontuacao_maquina += 1
        else:
            print("-" * 40) 
            print(f"VOCÊ GANHOU! VOCÊ: {opcao_jogador} CORTA CPU: {opcoes_jogo[jogada_maquina]} ")
            print("-" * 40)
            pontuacao_jogador += 1 

    elif(opcao_jogador == "PAPEL"):
         if(opcoes_jogo[jogada_maquina] == "TESOURA"):
            print("-" * 40) 
            print(f"VOCÊ PERDEU! CPU: {opcoes_jogo[jogada_maquina]} CORTA  VOCÊ: {opcao_jogador}")
            print("-" * 40)
            pontuacao_maquina += 1 
         else:
             print("-" * 40) 
             print(f"VOCÊ GANHOU! VOCÊ: {opcao_jogador} COBRE PEDRA CPU:{opcoes_jogo[jogada_maquina]}  ")
             print("-" * 40)
             pontuacao_jogador += 1

    else:
            print("-" * 40) 
            print("OPÇÃO DE JOGADA INVALIDA!")
            print("-" * 40)
    