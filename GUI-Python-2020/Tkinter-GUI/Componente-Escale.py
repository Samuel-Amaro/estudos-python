# COMPONENTE SCALE - COMPONENTE DESLIZANTE
# E UM COMPOENENTE DA SUBBIBLIOTECA TTK

from tkinter import *
from tkinter import ttk

# CRIANDO UMA JANELA
app = Tk()
app.title("SCALE")
app.geometry("500x300")

# CRIANDO UM LABEL
lbValor = Label(app,text="Valor")
# posicionando a label na janela
lbValor.pack()

# criando o componente scale
# Scale(componentePai,from_,to,orient)
# from = onde o escale começa, valor inicial
# to =  onde termina
# O ESCALE ABRANGE UMA FAIXA DE UMA ESCALA, TEM VALOR DE INICIO E VALOR FINAL, PARA COMPREENDER UM INTERVALO
# orient = HORIZONTAL , VERTICAL; DEFINE a HORIENTAÇÃO EM QUE A ESCALA VAI PODER SER CONTROLADA
scEscala = Scale(app,from_=0,to=100,orient=HORIZONTAL)
# posicionando o compoennte na janela
scEscala.pack()

# para poder definir um valor inicial no scale, ele se inicia com um valor inicial
scEscala.set(50)

# como obter um valor que foi definido pelo usuario usando scale
# funçaõ que vai imprimir o valor definido pelo usuario na scale
def valorEscala():
    # como obter uma valor do scale
    resultado = str(scEscala.get())
    print("Valor da Escala: " + resultado)

# criando um botão que vai mostrar o valor que o usuario definiu na escale
bt = Button(app,text="VALOR",command=valorEscala)
# posicionando o botão na janela
bt.pack()


app.mainloop()