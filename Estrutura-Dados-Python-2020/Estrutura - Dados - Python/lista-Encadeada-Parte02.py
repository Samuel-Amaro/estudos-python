from graphviz import Digraph # biblioteca graphivz para visualizar a lista encadeada em grafos

# DEMOSTRANDO COMO USAR UMA LISTA ENCADEADA - UMA ESTRUTURA DE DADOS LINEAR

listaEncadeada = []


# FUNÇÃO  QUE VAI ADICIONAR UM VALOR NA LISTA ENCADEADA
def addValorNo(valor,listaEncadeada):
    if(valor != 0):
       no = valor
       # se a lista esta vazia, a cabeça vai possuir um valor, criando a cabeça da lista, o inicio da lista, e o final da lista
       if(len(listaEncadeada) == 0):
          cabeca = valor
          cauda = valor
          listaEncadeada.insert(0,cabeca) # inserindo no inicio da lista
          listaEncadeada.append(cauda) # inserindo no final da lista 
       else:
           cauda = valor
           listaEncadeada.append(cauda) # atualizando o final da lista a cada nova inserção

# FUNÇÃO QUE VAI RETORNA DADOS IMPORTANTES DA LISTA
def getListaEncadeada(listaEncadeada):
    tamanhoLista = len(listaEncadeada)
    print('--------------------------------------------')
    print('           Dados Da Lista Encadeada        ')
    print('            Cabeça/Inicio = {}             '.format(listaEncadeada[0]))
    print('            Final/cauda = {}               '.format(listaEncadeada[tamanhoLista - 1]))
    print('Lista Completa: {}'.format(listaEncadeada))
    print('--------------------------------------------')

# função que renderiza a lista encadeada para consguir visualizar ela melhor na linguagem dot usando função Diagraph da biblioteca graphvz
def viewGraphList():
    global listaEncadeada
    dot = Digraph(comment='Lista-Encadeada')#adiciona um comentario na linguagem dot acima da função que renderiza o grafico
    print(dot) #para processar o comentario e o Digraph criado
    indice = 0; tmList = len(listaEncadeada); indice02 = 0
    #criando nos
    while(indice < tmList):
             dot.node(str(listaEncadeada[indice]))   
             indice += 1       
    #adiconado arestas entre os nos 
    while(indice < tmList):
         dot.edge(str(listaEncadeada[indice]),str(listaEncadeada[indice + 1]))
         indice += 1
    # vendo o codigo fonte gerado na linguagem dot
    print(dot.source)
    #mostrando o pdf gerado com a lista encadeada
    dot.render('arquivo-dot-gerado/lista-Encadeada.gv', view=True)  

# INSERINDOS VALORES NA LISTA, EM CADA NO
addValorNo(9,listaEncadeada);
addValorNo(12,listaEncadeada);
addValorNo(3,listaEncadeada);
addValorNo(7,listaEncadeada)
# IMPRIMINDO DADOS DA LISTA
getListaEncadeada(listaEncadeada)
#gerando o grafico da lista
viewGraphList()
