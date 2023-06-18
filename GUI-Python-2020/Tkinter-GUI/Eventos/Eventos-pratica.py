# EVENTOS NA PRATICA

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class TelaPrincipal:
        def __init__(self,principal):
                 # atributos da janela principal
                 self.tela = principal
                 self.tela.title="EVENTOS"
                 self.tela.geometry="500x300"
                 #atributo label da janela
                 self.lbl = Label(self.tela,text="Abrir Caixa",font=("verdana","16"),relief="raised")
                 self.lbl.pack(pady=20)
                 # tratador de eventos da label
                 # criando o bind do elemento que vai ocorrer o evento
                 #bind(evento,respotaAoEventoMetodoOuAção)
                 self.lbl.bind("<Button-1>",self.respotaEvento)

        #usuario clicou na label vou chamar o metodo resposta, recebendo o evento que ocorreu na label
        def respotaEvento(self,event):
            # mostra uma caixa de mensagem
            messagebox.showinfo("CAIXA DE MENSAGEM","VOCÊ CLICOU")            

App = Tk()

TelaPrincipal(App)

App.mainloop()