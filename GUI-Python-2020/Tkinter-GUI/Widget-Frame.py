# WIDGET DE TIPO FRAME(QUADRO, ARMAÇÃO)
# FRAME(e um componente de quadro, um componente organizacional, ele começa a criar quadros, atraves dele consegue organizar elementos dentro do formulario, separando por areas e tendo uma organização visual)


from tkinter import *
from tkinter import messagebox


#função que mostra uma caixa de mensagem de tipo informação
def mensagem():
    messagebox.showinfo(title="FRAME-QUADRO",message="UTILIZANDO QUADRO,\n PARA ORGANIZAR ELEMENTOS DENTRO DO FORMULARIO")


# criando formulario principal
app = Tk()
app.title("FORMULARIO")
app.geometry("500x300")
app.configure(background="#807642")

# CRIANDO UM QUADRO
# sintaxe:
# nomeObjeto = Frame('componente pai',borderwidth='espessura da borda',refief='estilo da borda')
# valores para o estilo da borda: #solid(borda solida) #flat(padrão) #raised(estilo 3d elevada) #sunken(3d fundo)
conteiner = Frame(app,borderwidth=1,relief="raised")
# configurando o conteiner dentro da janela, dando os valores de largura alltura onde deve ficar no formulario
conteiner.place(x=10,y=10,width=300,height=120)

# como add elementos dentro do frame

#crindo uma label que vai ter como seu componente pai o conteiner
lblMensagem = Label(conteiner,text="Digite uma Mensagem")
# configurando uma cor da fonte para label e uma cor de fundo da label
lblMensagem.configure(fg="#1A0D0B",background="#FAF9FC")
# posicionando o label dentro do conteiner
lblMensagem.place(x=10,y=10,width=150,height=20)


# criando uma caixa de entrada de texto que vai estar dentro do conteiner
txtMensagem = Entry(conteiner)
# posicionando o caixa de entrada de texto no conteiner
txtMensagem.place(x=10,y=50,width=150,height=20)


# criando um botão que vai ficar posicionaodo dentro do frame, o botão vai ter a tarefa de mostra uma caixa de mensagem ao ser clicado
btnMensagem = Button(conteiner,text="Ver Mensagem",command=mensagem)
# posicionando o botão dentro do conteiner do frame
btnMensagem.place(x=15,y=90,width=90,height=20)


# criando um segundo quadro com cor de fundo
conteiner2 = Frame(app,borderwidth=1,relief="raised",background="#102AE8")
# posicionando o conteiner dentro da janela
conteiner2.place(x=10,y=140,width=300,height=150)

#executando o formulario
app.mainloop()
