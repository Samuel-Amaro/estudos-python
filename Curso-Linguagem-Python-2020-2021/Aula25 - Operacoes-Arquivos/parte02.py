# APRENDER A LER O ARQUIVO PARA LEITURA, UM ARQUIVO JA EXISTENTE COM CONTEUDO, PARA SER LIDO NO MEU PROGRAMA, APRENDER A LER O CONTEUDO DE UM ARQUIVO

nomeArquivo = "arquivo_leitura.txt"

#ABRINDO ARQUIVO PARA LEITURA DO CONTEUDO

fileTeste = open("C:/Users/SAMUE/Documents/Programacao-Cursos-Projetos-2020/Curso-Linguagem-Python-2020/Aula25 - Operacoes-Arquivos/" + nomeArquivo,"rt")

# LEITURA DO CONTEUDO DO ARQUIVO USA A FUNÇÃO 
# arquivo.read()

#print(fileTeste.read())

# COMO LER UMA QUANTIDADE DE CARACTERES LIMITADO LER SO UMA QUANTIDADE ESPECIFICA DE CARACTERES DENTRO DO ARQUIVO DO CONTEUDO DO ARQUIVO
# arquivo.read(qtd caracteres)

#print("\n" + fileTeste.read(100))

# COMO LER UMA LINHA INTEIRA DO CONTEUDO DO ARQUIVO
# arquivo.readline() - le so uma linha de conteudo para ler varias tem que iterar a qtd de linha exata

#print("\n" + fileTeste.readline())

#lendo todo conteudo de um arquivo que eu não sei a qtd de linhas do arquivo
#for linhaArquivo in fileTeste:
#   print(linhaArquivo) 

# como cada linha do arquivo de conteudo e uma string eu posso manipulas as linhas ou so uma linha com string
#stringLinha = fileTeste.readline()
#print(stringLinha)

# FECHANDO ARQUIVO
fileTeste.close()

