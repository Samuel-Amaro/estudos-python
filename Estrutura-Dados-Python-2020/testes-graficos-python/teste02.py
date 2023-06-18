from graphviz import Digraph
dot = Digraph(comment='The Round Table')
dot  #doctest: +ELLIPSIS
dot.node('A', 'No 01')
dot.node('B', 'No 02')
dot.node('L', 'No 03')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source)
# The Round Table
digraph {
    A [label="No 01"]
    B [label="No 02"]
    L [label="No 03"]
    A -> B
    A -> L
    B -> L [constraint=false]
}
dot.render('test-output/round-table.gv', view=True) 
