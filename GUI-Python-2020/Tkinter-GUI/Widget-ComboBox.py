# WIDGET COMBOBOX

from tkinter import *
# importando o combobox que esta dentro de uma sub biblioteca
from tkinter import ttk


app = Tk()
app.title("COMBO BOX")
app.geometry("500x300")

# criando uma lista, que vai ser mostrada no comboBox
listMotos = ["Honda pop 100i","XRE-300","BROZ-160"]

# CRIANDO UMA LABEL
lbEsportes = Label(app,text="Motos Preferidas")
# add a label na janela
lbEsportes.pack()

# CRIANDO UM COMBO BOX VAZIO SEM NENHUM ITEM DA LISTA SELECIONADO INICIALMENTE
#ttk.ComboBox(componentePai,values=list)
cbEsportes = ttk.Combobox(app,values=listMotos)
# SETANDO UM ITEM NA LISTA, PARA QUANDO CRIAR O CB INICIALMENTE JA TER UM ITEM DA LISTA SELECIONADO
cbEsportes.set("XRE-300")
# posicionando um COMBOBOX na janela
cbEsportes.pack()

# criando uma função que vai pegar o item selecionado no combo box, e mostra no console para o usuario
def getMotos():
    # obter item selecionado no combo box cbEsportes.get()
    print("MOTO SELECIONADA: " + cbEsportes.get())

# criando um botão
btnMoto = Button(app,text="MOTO PREFERIDA",command=getMotos)
# posicionando o botão na janela
btnMoto.pack()


app.mainloop()