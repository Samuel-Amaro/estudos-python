"""
 # PARTE 02 SOBRE A TREE VIEW
  - APRENDER COMO INSERIR DADOS DE UM FORMULARIO NA TREE VIEW
  - COMO DELETAR DADOS SELECIONADOS DA TREE VIEW;
  - COMO OBTER UM REGISTRO SELECIONADO DA TREE VIEW;
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

app = Tk()
app.title("Tree View Parte 02")
app.geometry("500x300")



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


# como inserir dado na tree view ?
# usar o metodo insert
# treeview.insert('componentePai','onde vai inserir',values='valores')
# componentePai -> e a propria tree view
# onde vai inserir -> se e no inicio, no final no meio, num lugar especifico da tree view;
# values -> valores que vão ser inseridos na tree view



# CRIANDO UMA FORMULARIO COM 3 CAMPOS, PARA INSERIR DADOS DIRETAMENTE NA TREE VIEW

lbId = Label(app,text="ID",anchor=W)
txtId = Entry(app)
lbNome = Label(app,text="NOME",anchor=W)
txtNome = Entry(app)
lbFone = Label(app,text="TELEFONE",anchor=W)
txtFone = Entry(app)


# FUNÇÕES QUE DÃO AÇÃO PARA OS BOTOES
# metodo que faz inserção dos campos do formulario na tree view
def inserir():
    # obter elementos dos campos de texto
    # antes verificar se tem alguma coisa digitada nas caixas de texto
    if txtId.get() == "" or txtNome.get() == "" or txtFone.get() == "":
        # se os campos estiverem vazios mostra mensagem de erro
        mb.showinfo(title="ERRO",message="DIGITE TODOS OS DADOS")
    else:
        tv.insert("","end",values=(txtId.get(),txtNome.get(),txtFone.get()))
        #LIMPA CAMPOS
        txtId.delete(0,END)    
        txtNome.delete(0,END)
        txtFone.delete(0,END)

# metodo que faz, apagar um registro selecinado da tree view
# obter o elemento selecionado
def deletar():
    # treeview.selection() -> retorna uma tupla com os itens selecionados
    try:
        itemSelecionado = tv.selection()[0]
        # treeview.delete(item) -> apaga um registro da tree view informador por parametro para o delete
        tv.delete(itemSelecionado)
        print(itemSelecionado)
    except:
        mb.showinfo(title="ERRO",message="SELECIONE O ITEM SER DELETADO")
    
# metodo que obtem um registro selecionado da tree view
def obter():
    try:
        # obtendo registro selecionado
        itemSelecionado = tv.selection()
        # obtendo valores do item selecionado
        # treeview.item(itemSelecionado,option) -> RETORNA UMA TUPLA COM OS VALORES
        #option = opção values(mostra valores do item selecionado)
        valores = tv.item(itemSelecionado,"values")
        print(valores)
        # COMO OBTER VALORES ESPECIFICOS, LEMBRNADO QUE SÃO ARMAZENADOS EM UMA TUPLA, POSSO ACESSAR O INDICE DE CADA ITEM DA TUPLA PARA OBTER OQUE QUERO
        # index[0] = id
        # index[1] = nome
        # index[2] = fone
        print("INDICE 2: FONE: " + valores[2])
        print("INDICE 1 : NOME: " + valores[1])
    except:
        mb.showinfo(title="ERRO",message="erro ao obter item")
    



# botoes de inserir deletar e obter
btnInserir = Button(app,text="INSERIR",command=inserir)
btnDelete = Button(app,text="DELETAR",command=deletar)
btnObter = Button(app,text="OBTER",command=obter)

# posicionamento os elementos graficos na janela, com o sistema grid
lbId.grid(column=0,row=0,stick='w')
txtId.grid(column=0,row=1)
lbNome.grid(column=1,row=0,stick='w')
txtNome.grid(column=1,row=1)
lbFone.grid(column=2,row=0,stick='w')
txtFone.grid(column=2,row=1,stick='w')

tv.grid(column=0,row=3,columnspan=3,pady=5)

btnDelete.grid(column=0,row=4)
btnInserir.grid(column=1,row=4)
btnObter.grid(column=2,row=4)

app.mainloop()