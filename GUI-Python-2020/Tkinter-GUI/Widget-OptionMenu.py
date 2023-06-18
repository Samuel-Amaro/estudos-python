# WIDGET - OPTION MENU

from tkinter import *
from tkinter import ttk


# CRIANDO UMA JANELA PRINCIPAL
janela = Tk()
janela.title("WIDGET Option Menu")
janela.geometry("500x300")
janela.configure(background="#A1D6B8")

# criando uma label
lblTecnologias = Label(janela,text="Tecnologias")
lblTecnologias.pack()

# definindo uma variavel que vai receber os valores de cada opção escolhida no option menu, vai coletar o valor da opção escolhida no option menu
valorOp = StringVar()

# coletion - tipo list que define as opções do option menu
listOpcoesTecnologia = ["JAVA","C","PYTHON","HTML5","CSS3"]

# definido um valor padrão para o option menu, isso e sem o usuario selecinar nenhuma opçõa ja defino uma valor padrão
valorOp.set(listOpcoesTecnologia[2])


# criando um option menu - um menu de opções
# sintaxe:
# nomeObejto = OptionMenu('componente pai','variavel que  coleta opção escolhida no menu','list de opções para menu') # asteristico na list diz que quero mostrar todas opções

opTecnologia = OptionMenu(janela,valorOp,*listOpcoesTecnologia)
opTecnologia.pack()


# criando uma função que vai mostrar para o usuario qual opção foi escolhida no option menu
def getOpcaoMenu():
    t = valorOp.get()
    print("---------------------------------------------")
    print("JAVA - LINGUAGEM JAVA")
    print("C - LINGUAGEM C")
    print("PYTHON - LINGUAGEM PYTHON")
    print("HTML5 - DESENVOLVIMENTO DE PAGINAS HTML")
    print("CSS3 - DESENVOLVIMENTO DE ESTILOS DE PAGINA HTML")
    print("USUARIO ESCOLHEU: " + t)
    print("---------------------------------------------")

# criando um botão que vai ter ação de mostra para o usuario qual opção do menu ele escolheu
btnEscolheuTecnlogia = Button(janela,text="EU ESCOLHI ?",command=getOpcaoMenu)
btnEscolheuTecnlogia.pack()


# executando aplicação grafica
janela.mainloop()