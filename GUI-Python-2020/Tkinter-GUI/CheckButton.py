# WIDGET - CHECKBUTTON

from tkinter import *

app = Tk()
app.title("CHECKBUTTON")
app.geometry("500x300")

# criando um conteiner
conteiner_1 = Frame(app,borderwidth=1,relief="solid")
# add o conteiner a janela
conteiner_1.place(x=10,y=10,width=300,height=100)

# variaveis que vão armazenar os valores que os chekcbutton possui
vFutebol = StringVar()
vVolei = StringVar()
vBasquete = StringVar()

# criando uma funçaõ que vai dar uma ação para o check buton ao ele ser clicado ou selecionado por usuario
def futebolAcao():
    print("Goll do flamengo.......")

# criando uma funçaõ que vai dar uma ação para o check buton ao ele ser clicado ou selecionado por usuario
def voleiAcao():
    print("Ponto do barueri")    

# criando uma funçaõ que vai dar uma ação para o check buton ao ele ser clicado ou selecionado por usuario
def basqueteAcao():
    print("Cesta 3 pontos Jordam")    

# criando um checkbutton
# Checkbutton(widgetPai,text,variable,onvalue,offvalue,command)
# variable = armazena o valor que o checkbutton possui
# onvalue = valor quando o checkbutton estiver selecionado
#offvalue = valor quando checkbutton não estiver selecionado
# quando varivel vFutebol estiver em sim, significa que o componente esta selecionado, quando tiver em não o componente não esta selecionado
# commad = comando para que ao selecionar o check button ele efetue uma interação ou ação, por meio do comand ele excuta a sua interação;
# ao o botão ser clicado ele efetue uma ação
cb_futebol = Checkbutton(conteiner_1,text = "Futebol",variable = vFutebol,onvalue="sim",offvalue="não",command=futebolAcao)
# add o ckeck button ao conteiner 
cb_futebol.pack(side=LEFT)

# criando um check button de volei
cbVolei = Checkbutton(conteiner_1,text = "Voleibol",variable = vVolei,onvalue="sim",offvalue="não",command=voleiAcao)
# add o check button ao conteiner
cbVolei.pack(side=LEFT)

# criando um check button de basquete
cbBasquete = Checkbutton(conteiner_1,text = "Basquete",variable = vBasquete,onvalue="sim",offvalue="não",command=basqueteAcao)
# add o check button ao conteiner
cbBasquete.pack(side=LEFT)

app.mainloop()
