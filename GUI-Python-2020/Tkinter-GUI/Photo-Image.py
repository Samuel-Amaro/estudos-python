"""
 # APRENDER COMO INSERIR IMAGENS NO FORMULARIO
"""
from tkinter import *
import os

pastaApp = os.path.dirname(__file__) # caminho onde o programa esta rodando

formulario = Tk()
formulario.title("trabalhando com imagens")
formulario.geometry("500x300")

# PhotoImage e como so a caixa da imagen, so define o espaço da imagen inicialmente, não e onde a imagen vai ficar no formulario
img = PhotoImage(file=pastaApp+"\\download.png")

# label que vai armazenar a imagen
labelImagen = Label(formulario,image=img)

# posicionando onde o label vai ficar dentro do formulario
labelImagen.place(x=10,y=10)

formulario.mainloop()