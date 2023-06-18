"""
 # COMPONENTE WIDGET = TREE VIEW
  - COMPONENTE DO TIPO GRADE DE LISTAGEM
  - mostra conteudo de uma lista ou de um banco de dados
"""

from tkinter import *
from tkinter import ttk

app = Tk()
app.title("Tree View Parte 01")
app.geometry("500x300")

# cria uma matriz(cada item da lista e uma nova lista)
matrizPessoas = [
               ['0','Juninho','61 99999-0000'],
               ['1','Hellen','61 22222-0000'],
               ['2','Renata Fan','61 99999-8888'],
               ['3','Rogerio Ceni','61 99999-2222']
              ]

# colocar essa matriz acima dentro da treeview


# criando a treeview
# ttk.Treeview(componentePai,columns=(colunas) show="opção")
# columns -> colunas que a tree view vai ter, as colunas são informadas, os nomes de cada coluna, e separado por virgula;
# show -> mostra alguma coisa, a opçaõ headings, vai mostra o cabeçalho da tree view
tv = ttk.Treeview(app,columns=('id','Nome','Fone'), show="headings")

# definindo largura das colunas
# largura minima e maxima, e a coluna pode ser redimensionada
#treeview.column('nomeColuna',minwidth='largura minima',width='largura maxima')

tv.column('id',minwidth=0,width=50)
tv.column('Nome',minwidth=0,width=250)
tv.column('Fone',minwidth=0,width=100)

# definindo os textos que vão apararecer no cabeçalho da tree view
# configurando os textos que vão aparecer nas colunas
# treeview.heading('nomeColuna',text="oque vai aparecer")
tv.heading('id',text="ID")
tv.heading('Nome',text="NOME")
tv.heading('Fone',text="TELEFONE")

# posicionando a tree view na janela, usando o metodo de posicionamento pack
tv.pack()

# como inserir dado na tree view ?
# usar o metodo insert
# treeview.insert('componentePai','onde vai inserir',values='valores')
# componentePai -> e a propria tree view
# onde vai inserir -> se e no inicio, no final no meio, num lugar especifico da tree view;
# values -> valores que vão ser inseridos na tree view

# inserido os dados da matriz na tree view
for (itemId,itemNome,itemFone) in matrizPessoas:
    tv.insert("","end",values=(itemId,itemNome,itemFone))

app.mainloop()