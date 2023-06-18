
# teste que cria um grafo-usando a linguaguem dot usando o pacote graphivs para formar o pdf com o grafico
from graphviz import Digraph
dot = Digraph(comment='Grafico teste')
print(dot)
dot.node('A', 'No 01')
dot.node('B', 'No 02')
dot.node('L', 'No 03')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source)
dot.render('test-output/grafico-teste.gv', view=True) 