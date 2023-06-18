import os

# COMO DELETAR UM ARQUIVO 

nomeArquivo = "arquivo_teste_01.txt"
caminhoArquivo = "C:/Users/SAMUE/Documents/Programacao-Cursos-Projetos-2020/Curso-Linguagem-Python-2020/Aula25 - Operacoes-Arquivos/"


# VERIFICA ANTES SE O ARQUIVO EXISTE
if (os.path.exists(caminhoArquivo + nomeArquivo)):
    print("Arquivo existe")
else:
    # CRIANDO O ARQUIVO
    fileTeste = open(caminhoArquivo + nomeArquivo,"x")

# VERIFICA ANTES SE O ARQUIVO EXISTE
if (os.path.exists(caminhoArquivo + nomeArquivo)):
    print("Removido")
else:    
#EXCLUINDO O ARQUIVO
    os.remove(caminhoArquivo)
    print("Arquivo Removido")

#FECHANDO ARQUIVO
fileTeste.close()