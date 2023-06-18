# PARTE 02 DA AULA ABRINDO UM NOVO FORMULARIO E PASSANDO ARGUMENTOS
# AQUI VAI SER CONFIGURADA A JANELA SECUNDARIA A QUE VAI SER ABERTA A PARTIR DE UMA JA EXISTENTE E FUNCIONANDO;

from tkinter import *

# istanciando uma nova janela, a JANELA SECUNDARIA
janelaSecundaria= Tk()

# mostrando o parametro que a janela secundaria recebe, esse parametro veio da janela principal, foi passado um parametro para essa janela, mostrando esse parametro
print("valor do parametro que a janela secundaria recebe: " + str(x))

# dando um titulo para a janela
janelaSecundaria.title("JANELA SECUNDARIA")

# configurando o tamanho da janela
janelaSecundaria.geometry("500x300")

# configurando uma cor de fundo da janela secundaria
janelaSecundaria.configure(background="#38B327")

# executando o programa de interface grafica, chamando a janela o formulario para ser executado
janelaSecundaria.mainloop()
