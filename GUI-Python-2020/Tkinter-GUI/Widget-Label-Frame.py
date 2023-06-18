# COMPONENTE WIDGET LABEL FRAME

from tkinter import *

# criado uma janela
app = Tk()
app.title("LABEL FRAME")
app.geometry("500x300")


# criando um label frame
# LabelFrame(componentePai,text)
# o text vai ser o label do frame
lbFrame = LabelFrame(app,text="LABEL FRAME",borderwidth=1,relief="solid")

# posicionando o label frame na janela
lbFrame.place(x=10,y=10,width=300,height=100)


# criando uma label
lb = Label(lbFrame,text="TESTANDO")
# posicionando a label dentro do label frame
lb.pack()

app.mainloop()