# WIDGET ABAS NOTEBOOK

from tkinter import *
from tkinter import ttk

# criado uma janela
app = Tk()
app.title("ABAS NOTEBOOK")
app.geometry("500x300")

"""
 * PARA SE TRABALHAR COM ABAS TEM QUE CRIAR UM ELEMENTO NOTEBOOK;
 * QUE SERVE PARA GERENCIAR AS ABAS;
 * E COM OS NOTEBOOK PODE-SE CRIAR OS FRAMES, E ADD COMO PAI DE CADA FRAME UM NOTEBBOK;
 * AI BASTA CRIAR O CONTEUDO QUE EU QUERO PARA CADA FRAME E COLOCAR COMO PAI DESSE CONTEUDO O FRAME
"""

# criando um notebook
# ttk.Notebook(componentePai)
nb = ttk.Notebook()
# posicionando o notebook na janela
nb.place(x=0,y=0,width=500,height=300)


# LEMRBANDO QUE CADA FRAME VAI SER UMA ABA

#CRIANDO UM FRAME
fm1 = Frame(nb)

# add o frame ao notebook
# notebook.add(quemVouAdd,textoParaAba)
nb.add(fm1,text="TESTE ABA 1")

# add mais uma aba

# criando uma frame
fm2 = Frame(nb)

#add o frame ao notebook
nb.add(fm2,text="TESTE ABA 2")


# add conteudo nas abas

#add umas labels na aba 1

# criando uma label de conteudo para a aba 1
lb1 = Label(fm1,text="UM CONTEUDO")
# posicionando a label na aba 1
lb1.pack()

# add conteudo na aba 2z

# criando uma label de conteudo para a aba 2
lb2 = Label(fm2,text="UM CONTEUDO PARA A ABA 2")
# posicionando a label na aba 1
lb2.pack()


app.mainloop()