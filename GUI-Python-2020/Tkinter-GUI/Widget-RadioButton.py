# WIDGET - RADIOBUTTON


from tkinter import *
# import elementos componentes visuaus mais modernos do tkinter
from tkinter import ttk


# criando uma janela principal
janelaPrincipal = Tk()
janelaPrincipal.title("WIDGET RADIO BUTTON")
janelaPrincipal.geometry("500x300")
janelaPrincipal.configure(background="#A1D6B8")


# criando uma label que vai da um titulo para o grupo de radio buttons
lblEsporte=Label(janelaPrincipal,text="Esportes")
lblEsporte.pack()


# como posso fazer ou dizer que os radio buttons a seguir são um conjunto de elementos, quero ele agrupados, porque eles pertecem a um mesmo contexto então são muitos parecidos
# cria se um elemento do tk variavel = StringVar()
# ele vai determina que esse elemento e uma variavel, ele vai se associar aos elementos, para poder receber o valor desses elementos

valorEsporte = StringVar()


#criando os radiobuttons, cada radio button da uma opção de esporte
# sintaxe:
# nomeObejto = Radiobutton('componente pai',text = 'texto que aparece no radio button',value = 'valor que o radio button tem ao ser escolhido um valor que ele possui, eu que defino',variable = 'variavel que recebe o valor do radioButton tem que possuir um stringVar associado')

rbFutebol = Radiobutton(janelaPrincipal,text="Futebol",value="f",variable=valorEsporte)
rbFutebol.pack()
rbVolei = Radiobutton(janelaPrincipal,text="Vôlei",value="v",variable=valorEsporte)
rbVolei.pack()
rbTenis = Radiobutton(janelaPrincipal,text="Tênis",value="t",variable=valorEsporte)
rbTenis.pack()


# criando uma função que vai mostrar qual esporte foi selecionado pelo usuario atraves do radio button
def getEsporte():
    ve = valorEsporte.get()
    print("-------------------------------")
    print("Valor de esporte escolhido foi")
    print("f - Futebol")
    print("v - volei")
    print("t - tenis")
    print("Usuario escolheu: " + ve)
    print("-------------------------------")


# criando uma botão que vai ter a função de que ao ser clicado vai mostrar para o usuario qual esporte ele escolheu atraves do radio button
btnGetEsporte = Button(janelaPrincipal,text="Meu Esporte e ?",command=getEsporte)
btnGetEsporte.pack()


# executando aplicação grafica
janelaPrincipal.mainloop()