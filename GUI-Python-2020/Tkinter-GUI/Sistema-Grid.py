# SISTEMA GRID - UMA MANEIRA DE POSICIONAR OS ELEMENTOS ALEM DO PACK DO PLACE PODEMOS USAR O GRID
# SISTEMA GRID

from tkinter import *
from tkinter import ttk

# criado uma janela
app = Tk()
app.title("SISTEMA DE GRID")
app.geometry("500x300")

# CRIANDO UMS ELEMENTOS E POSICIONANDO ESSE ELEMNTOS NA JANELA PRINCIPAL, USANDO O SISTEMA DE GRID

# CRIANDO ELEMENTOS DO TIPO LABEL E ENTRY

# CRIANDO UM LABEL NOME
lbNome = Label(app,text="SEU NOME")

# CRIANDO UMA LABEL IDADE
lbIdade = Label(app,text="SUA IDADE")

#CRIANDO UMA LABEL EMAIL
lbeEmail = Label(app,text="SEU E-MAIL")

# CRIANDO CAIXAS DE TEXTO, CAIXAS DE ENTRADA DE TEXTO, EM QUE USUARIO DIGITA UM TEXTO

# caixa de texto nome
txtNome = Entry(app)

# caixa de texto idade
txtIdade = Entry(app)

# caixa de texto email
txtEmail = Entry(app)


# CRIANDO UM BOTÃO CADASTRAR
btnCadastrar = Button(app,text="CADASTRAR")

# PARA USAR O SISTEMA DE GRID E MUITO TRANQULO, COMO ELE FUNCIONA ? BASTA INDICAR O ELEMENTO QUE QUERO POSICIONAR, E DIZER EM QUAL LINHA E COLUNA QUERO, QUE O ELEMENTO FIQUE NA JANELA

# POSICIONANDO OS ELEMENTOS CRIADOS USANDO O GRID
# elemento.grid(column,row,sticky,columnspan,rowspan,padx,pady)
# coluna = numero da coluna
# row = linha numero da linha
# sticky = alinhamento do elemento dentro da sua linha e coluna opções de alinhamento, posição dentro do grid, onde o elemento se posiciona dentro da celula do grid: norte = n -> (topo),sul = s ->(baixo),leste = e ->(direita), oeste = w -> (esquerda)
# columnspan = faz a mesclagens de colunas informadas, isso e junta duas ou mais colunas para posicionar o elemento
# rowspan = para mesclar linhas, duas ou mais linhas informadas para mesclar o elemento entre as linhas
#padx = espaço interno na horizontal da celula do sistema de grid
# pady = espaço interno na vertical da celula do grid


# posição coluna 0 linha 0 alinhamento esquerda
lbNome.grid(column=0,row=0,sticky='e',pady=30)

#posição coluna 0 linha 1 alinhamento direita
txtNome.grid(column = 1,row=0,sticky='w')

## posição coluna 0 linha 2 alinhamento esquerda
lbIdade.grid(column=0,row=2,sticky='w',padx=5)

#posição coluna 0 linha 3 alinhamento direita
txtIdade.grid(column=0,row=3,sticky='e')

# posição coluna 0 linha 4 alinhamento esquerda
lbeEmail.grid(column=0,row=4,sticky='w')

#posição coluna 1 linha 5 alinhamento direita
txtEmail.grid(column=0,row=5,sticky='e')


app.mainloop()