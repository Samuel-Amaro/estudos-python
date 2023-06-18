# WIDGET LISTBOX

from tkinter import *

# criado uma janela
app = Tk()
app.title("LABEL FRAME")
app.geometry("500x300")

# CRIANDO UMA LISTA COM ELEMENTOS
listMotos = ["BIZ 125","POP 110i","BIZ 110i","BROZ 160","XRE 300"]

# criando uma list box
#Listbox(componentePai)
lbMotos = Listbox(app)

# inserindo os elemntos da lista no widget list box
for elemento in listMotos:
    # inseri sempre ao final da lista um novo elemento
    #listbox.insert(ONDENALISTAINSERIR,OQUEINSERIR)
    lbMotos.insert(END,elemento) 

# poscionando o listbox na janela
lbMotos.pack()


#função que vai pegar o item selecinado no list box e mostra para o usuario qual item foi selecionado
def getMoto():
    # COMO OBTER O ITEM SELECIONADO NO LIST BOX ?
    #listbox.get(ELEMENTO_SELECIONADO_ATIVADO)
    resultadoItem = str(lbMotos.get(ACTIVE))
    print("A MOTO SELECIONADA FOI: " + resultadoItem)

# criando um botão,esse botao vai mostrar o esporte selecionado, no listbox
btnMoto = Button(app,text="MOTO",command=getMoto)

# POSICIONANDO O BOTÃO NA JANELA
btnMoto.pack()

# como inserir novos elementos no list box ?

# obtendo o elemento do usuario, atraves de uma caixa de input text
inputElemento = Entry(app)
# posicionando caixa de texto
inputElemento.pack()

# função que inseri um novo elemnento no list box
def setMoto():
    # como inserir um novo elemento no listBox ?
    # esse elemento veio da caixa de entrada de texto
    lbMotos.insert(END,inputElemento.get())

# criando um botão,esse botao vai mostrar o esporte selecionado, no listbox
btnNovaMoto = Button(app,text="NOVA MOTO",command=setMoto)

# POSICIONANDO O BOTÃO NA JANELA
btnNovaMoto.pack()



app.mainloop()