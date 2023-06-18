# WIDGET SPINBOX

from tkinter import *

# criado uma janela
app = Tk()
app.title("LABEL FRAME")
app.geometry("500x300")

# CRIANDO UM SPIN BOX
#SpinBox(componentePai)
# 2 maneiras de se trabalhar com o spin box
# 1ª maneira: indica qual e a faixa de valores, indicar qual e o valor inicial(from_), qual e o valor final(to), utiliza essa forma quando a faixa de valor e grande;
    # Spinbox(componentePai,from_,to)
#sbValores = Spinbox(app,from_=0,to=100)
# add o spin box a janela
#sbValores.pack()

# outra maneira de se trabalhar com o spin box definindo os valores, usando a propriedade values, determina uma faixa de valores especificas
sbValores = Spinbox(app,values=(1,2,3,4,5))
# add o spin box a janela
sbValores.pack()


# como pegar o valor do spin box ?

# função que pega o valor do spin box e mostra para o usuario atraves de um clique em um botão
def getValor(): 
    # como obter um valor de um spin box ?
    #valor = sbValores.get()
    print("Valor: " + str(sbValores.get()))


# usando um botão que ao ser clicado vai pegar o valor escolhido pelo usuario no spin box, e mostrar ao usuario
btnValor = Button(app,text="VALOR",command=getValor)
#posicionando o botão na janela
btnValor.pack()


app.mainloop()