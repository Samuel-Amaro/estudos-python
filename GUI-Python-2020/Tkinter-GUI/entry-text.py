# COMPONENTES DE ENTRADA DE TEXTO ATRAVES DA INTERFACE GRAFICA, COMPONENTES QUE CAPTURA TEXTO DE ENTRADA DO USUARIO

from tkinter import *
# O segundo, "ttk" , é a vinculação do Python aos "widgets temáticos" mais novos que foram adicionados ao Tk em 8.5.
from tkinter import ttk

# criando minha janela
janela = Tk()

#titulo da janela
janela.title("Entrada de Texto")

# tamanho da janela
janela.geometry("400x400")

#cor de fundo
janela.configure(bg="#dde")

#criando uma label nome
lblNome = Label(janela,text="Nome",background="#dde",foreground="#009",anchor=W)
#paramentro anchor(com as indicações cardiais posso indicar em que sentido quero que fique a minha ancora o texto dentro da label) - opções:
#N=Norte,S=Sul,E=Leste,W=Oeste,NE=Nordeste,SE=SUDESTE,SO=Sudoeste,NO=NOROESTE

# dizenodo aonde quero que minha label fique dentro da janela, dando o posicionamento dela
lblNome.place(x=5,y=20,width=200,height=10)
# executando a janela

#componente que recebe uma entrada de texto de uma linha so, serve para entrada de texto simples de uma so linha sem quebra
#intancia objeto e no costrutor da o seu componente pai
getNome = Entry(janela)
# posicionamento do Entry
getNome.place(x=5,y=40,width=200,height=20)


# criando uma label telefone
lblTelefone = Label(janela,text="Telefone",background="#dde",foreground="#009",anchor=W)
#posicionamento da label telefone
lblTelefone.place(x=5,y=80,width=200,height=10)
#componente que recebe uma entrada de texto de uma linha so, so para texto simples
getTelefone = Entry(janela)
#posicionamento
getTelefone.place(x=5,y=100,width=200,height=20)

#criando uma label email
lblEmail = Label(janela,text="Email",background="#dde",foreground="#009",anchor=W)
# posiscionamento da label email
lblEmail.place(x=5,y=140,width=200,height=10)
#criando um componente de entrada de texto simples so de uma linha
getEmail = Entry(janela)
# posicionamento da caixa de entradada de texto
getEmail.place(x=5,y=160,width=200,height=20)



# criando uma label
lblObs = Label(janela,text="Obs",background="#dde",foreground="#009",anchor=W)
# posicionamento da label
lblObs.place(x=5,y=200,width=200,height=10)

# criando uma caixa de entradada de texto do tipo Text, uma caixa que pode receber um texto com varias linhas, o usuario pode digitar um texto de varias linhas
# componente de multiplas linhas
# objeto = Text('componente pai')
getObs = Text(janela)
getObs.place(x=5,y=220,width=350,height=100)
janela.mainloop()