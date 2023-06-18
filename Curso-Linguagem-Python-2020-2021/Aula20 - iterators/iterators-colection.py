# AULA 20 - ITERATORS
# O ITERATORS E UM OBJETO QUE PODE SER ITERADO(PERCORRIDO), PODE PERCORRER VALORES DE UMA COLEÇÃO, ACESSA, AVANÇA EM VALORES DE UMA COLEÇÃO
# UMA COLETION SÃO AS LIST,TUPLAS,DICTIONARY ETC...


# CRIANDO UMA COLEÇÃO DE TIPO LIST
times = ['Flamengo','Corinthias','Vasco','Atletico MG','Goias']

# COMO ACESSAR OS VALORES DESSA COLECTION ? FAZENDO ISSO DE MANEIRA TRADICIONAL, ACESSANDO VALORES, ATRAVES DE UMA ITERAÇÃO DE UM LOOP
for valor in times: #valor vai recebe cada item da list times
    print(valor)

# COMO PERCORRER A LIST USANDO UM ITERATORS
"""
SINTAXE:
  objeto_iterator = iter(list_que_vai_Ser_iterada_ou_coletion) 
  a função iter implementa __next__ __iter__
"""    
# criando o iterators
iterFutebol = iter(times)

# percorrendo a list com iterators usando o metodo next() - vai imprimir cada item da list a cada chamada do metodo next dentro do print - next(iterator_coletion)
print(next(iterFutebol))
print(next(iterFutebol))
print(next(iterFutebol))
print(next(iterFutebol))
print(next(iterFutebol))


# usando o iterators dentro de um loop while 
while(iterFutebol):
    try:
        print(next(iterFutebol))
    except:
        print('Fim da List')
        break