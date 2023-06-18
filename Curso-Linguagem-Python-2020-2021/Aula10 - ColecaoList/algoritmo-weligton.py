def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro: por favor, digite um número inteiro válido:\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m ')
            return 0
        else:
            return n


def leiaStr(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError, NameError):
            print('\033[31mErro: por favor, digite um nome válido (Letras):\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m ')
            return 0
        else:
            return n
'''
from criticalpath import Node
p = Node ('Projeto_TCC')
a = p.add(Node('A', duration= 10))
b = p.add(Node('B', duration= 30))
c = p.add(Node('C', duration= 10))
d = p.add(Node('D', duration= 40))
e = p.add(Node('E', duration= 30))
f = p.add(Node('F', duration= 20))

p.link(a, b) .link(a, c) .link(b, d) .link(c, e) .link(d, f) .link(e, f)

p.update_all()

print(f'O caminho crítico é: {p.get_critical_path()}.')
print(f'Possui duração de {p.duration} dias.')

'''

from criticalpath import Node
Qnt_atividade = leiaInt('Digite a quantidade de atividades: ')
p = Node('Projeto_TCC')
caminho = [] # list vazia quando não tem predecessora
tarefas = []
caminho_predecessora = {}
lista_predecessora = []
for atividade in range (Qnt_atividade):
    print('---'*10)
    tarefa = input('Digite o nome da tarefa: ')
    duração = int(input(f'Digite a duração da tarefa {tarefa}:  '))
    nó = p.add(Node(tarefa.upper(), duration=duração))
    #tarefas.append(nó)
    pred = input('Digite quantidade de predecessora: .Obs: caso não tenha digite espaço e Enter: ')
    if pred == ' ': #sempre que não tiver predecessora será a primeira atividade do caminho;
        caminho.append(pred)
    else:
        n = int(pred)
        for i in range (n):
            prede = input(f'Digite a precessora da atividade {tarefa}: ')
            #chave=predecessora:valor=tarefa
            caminho_predecessora = {prede:tarefa}
            lista_predecessora.append(caminho_predecessora)

# itera sobre a lista predecesora        
for i in lista_predecessora:
    print(i)

#mostra quantidade de p links a criar
qtdLinks = len(lista_predecessora)


#print(lista_predecessora)    
#p.update_all()
#print(p.get_critical_path())

    #nó = p.add(Node(tarefa.upper(), duration = duração))
    #tarefas.append(nó)

#for k, v in caminho_predecessora.items():


#for i in tarefas:

#p.link(tarefas[0], tarefas[1]) .link(tarefas[0], tarefas[2]) .link(tarefas[1], tarefas[3]) .link(tarefas[2], tarefas[4]) .link(tarefas[3], tarefas[5]) .link(tarefas[4], tarefas[5])

#p.link(a, b) .link(a, c) .link(b, d) .link(c, e) .link(d, f) .link(e, f)



#print(p.duration)