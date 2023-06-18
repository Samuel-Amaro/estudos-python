# WIDGET PROGRESS BAR - BARRA DE PROGRESSO

from tkinter import *
from tkinter import ttk

# criado uma janela
app = Tk()
app.title("BARRA DE PROGRESSO")
app.geometry("500x300")

# varivel que vai armazenar o valor inicial da barra, vai armazenar o valor da barra de progresso
# o valor que for definido nessa variavel, e o valor que vai ser apresentado na barra de progresso
varBarra=DoubleVar()
varBarra.set(0)

# CRIANDO A PROGRES BAR
# ttk.Progressbar(componentePai,variable=variavelValor,maximum)
# variavelValor = vai se uma varivel que vai conter um valor, que vai dizer em que lugar a barra de progresso tem que se posicionar, vai conter o valor da progress bar
# maximun = valor maximo em que a barra pode chegar
pb = ttk.Progressbar(app,variable=varBarra,maximum=100)

#posicionando a barra de progresso na janela
pb.place(x=0,y=0,width=500,height=40)

# TODA VEZ QUE QUISER ATUALIZAR A POSIÇÃO DA BARRA, TEM QUE ATUALIZAR A VARIAVEL DE CONTROLE DA BARRA, A VARIVEL QUE DEFINE O VALOR EM QUE A BARRA DEVE SE POSICIONAR

# EXEMPLO DEFININDO A POSIÇÃO DA BARRA ESTATICAMENTE:

# FUNÇÃO QUE VAI DEFINI UM VALOR EM QUE A BARRA DEVE SE POSICONAR
def setValorBarra():
    varBarra.set(50)
    

# CRIANDO UM BOTÃO, QUE AO SER CLICADO ELE VAI DEFINIR ESTATICAMENTE ONDE A POSIÇÃO DA BARRA DEVE SE POSICIONAR
bt = Button(app,text='DEFINIR BARRA',command=lambda:setDinaBar(10000))
# posicionando o botão na janela
bt.place(x=10,y=60,width=100,height=20)


# COMO DEFINIR A POSIÇÃO DA BARRA DE MANEIRA DINAMICA, DE UMA MANEIRA QUE DE PARA VER ELE CRESCENDO, PARA VER A BARRA EM PROGRESSÃO, VER A BARRA SENDO PREECHIDA PROGRESSIVAMENTE

# FUNÇAÕ QUE POSICIONA A BARRA DE MANEIRA DINAMICA
def setDinaBar(valorMaximo):
    contador = 0;contadorInterno = 0;
    etapas = valorMaximo / 100
    while contador < etapas:
          contador = contador + 1
          while contadorInterno < 1000000:
               contadorInterno = contadorInterno + 1
          # atualizando a barra de progresso onde ela deve se posicionar
          varBarra.set(contador)
          # dando um update no app na janela principal, para que a cada posiçaõ da barra a janela se redesenhe e mostre a barra de progresso com o efeito de evolução
          app.update() # redesenha a tela principal



app.mainloop()