# TRABALHAR COM LEITURA CRIAÇÃO E ESCRITA DE ARQUIVOS EXTERNOS EM PYTHON

# COMO ABRIR O ARQUIVO EM MEU PROGRAMA
# USAR A FUNÇÃO OPEN
# varivavel = open('caminho ate arquivo nome.extensão','modo de abertura')

# MODOS DE ABERTURA:
# r - read(leitura) - para ler o arquivo em meu programa - abre o arquivo so no modo de leitura
# a - append(anexar, adicionar um novo conteudo no final do arquivo) - abre o arquivo para o modo de receber um novo conteudo
# w - write - (escrita escrever no arquivo, abre o arquivo no modo de escrita nele)
# x - create - criar o arquivo - so cria o arquivo - so abre o arquivo e cria ele no local indicado
# t - modo texto - text pode omitir porque e padão
# b - modo binario
# CRIANDO UM ARQUIVO

fileTeste = open('C:/Users/SAMUE/Documents/Programacao-Cursos-Projetos-2020/Curso-Linguagem-Python-2020/Aula25 - Operacoes-Arquivos/arquivo-teste.txt','wt')

# COMO ESCREVER UM TEXTO DENTRO DO ARQUIVO
# USA A FUNÇÃO write
# arquivo.write('oque quero escrever no arquivo')
# \n quebra uma linha - programador que contrala a indentação do texto e aparencia

fileTeste.write('Samuel Amaro\n')
fileTeste.write('Testando um arquivo externo que eu crie atraves do Python usando operações de arquivos ensinado pelo CBF cursos\n')

# ESCREVENDO UM INPUT NO ARQUIVO

txtEntrada = input('Digite um Texto: ')

# ADD INPUT AO MEU ARQUIVO
fileTeste.write(txtEntrada + '\n')

# FECHA O ARQUIVO CRIADO, TODO ARQUIVO ABERTO, APOS USADO, FEITO TUDO QUE TINHA QUR FAZER TEM QUE FECHAR O ARQUIVO, SE NÃO NÃO SALVA AS MODIFICAÇÕES NO ARQUIVO

fileTeste.close()