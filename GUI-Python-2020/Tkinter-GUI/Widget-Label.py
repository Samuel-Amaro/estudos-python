# WIDGET (COMPONENTE VISUAL)
# LABEL(ROTULO - MOSTRA UM TEXTO DE UMA LINHA PARA O USUARIO)

from tkinter import *


#criando um formulario
formulario = Tk()
formulario.title("CONFIGURANDO LABEL")
formulario.geometry("500x300")

# criando um grado um conteiner
conteiner = Frame(formulario,borderwidth=1,relief="sunken")
# posicionando o conteiner no formulario
conteiner.place(x=100,y=40,width=300,height=200)
# configurando uma cor de fundo para o conteiner
conteiner.configure(background="#3F1FFF")


# criando uma label que vai ter seu posicionamento dentro do conteiner, vai ser posicionada dentro do conteiner
lblTexto = Label(conteiner,text="WELINGTON CABEÇÃO")
# configurando uma cor de fundo para label, uma cor para a fonte, e configurando a fonte e tamanho
lblTexto.configure(foreground="#FFFFFF",background="#3F1FFF",font=("Arial",19))
# configurando o posicionamento da label dentro do conteiner, quero a label centralizada na horizontal
# side - lado em que o label vai ficar dentro do conteiner = 'left,right,top,button'
# fill = X,Y (COMO A LABEL DEVE SER PRENCHIDA NO CONTEINER, NA HORIZONTAL(x) OU VERTICAL(Y))
# expand = true(pode expandir se redimensionar se o conteiner crescer ou diminuir) false(label fica estatica, tamanho normal sem redimensionamento)
lblTexto.pack(side=LEFT,fill=X,expand=TRUE)


# executando formulario
formulario.mainloop()