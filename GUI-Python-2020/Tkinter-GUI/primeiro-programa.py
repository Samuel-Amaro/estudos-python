from tkinter import * # importa a biblioteca grafica, todos os seus widgets(elementos graficos) para poder usar no arquivo

# criando uma janela | intanciando um objeto janela da classe Tk() 
# nome_janela = Tk()

# intanciando uma nova janela limpa vazia sem nenhum elemento 
app_teste = Tk()

# dando um titulo para a janela
app_teste.title("Teste Janela")

# configurando o tamanho da janela
# sintaxe
# objetoJanela.geometry("largura X altura")
app_teste.geometry("500x300")

#como adicionar uma cor de fundo na janela
# sintaxe
# objetoJanela.configure(background="corRGB")
app_teste.configure(background="#008")

# como inserir elementos widgets dentro dessa janela que eu criei
# cria o elemento e indico a esse elemento que e o pai do elemento e onde ela vai ficar


# criando uma label
# nomeObejtoLabel = label('pai da label','configurações da label')
txt1 = Label(app_teste,text="Primeira Janela Python",background="#ff0",foreground="#000")

# colocando o meu label dentro da minha janela dizendo a onde ele tem que se localizar e ficar dentro da janela, uma maneira de posicioanamento de elementos quando não se tem conteiner para colocar os elementos
#place == lugar,colocar na janela
# objetoLabel.place('posicoes de dimensionamento')
# x = posição horizontal
# y = posição vertical
# whidth = largura da label
# height = altura da label
txt1.place(x=10,y=10,width=150,height=30)

#PODE DEFINIR AS VARIAVEIS DE CONFIGURAÇÕES PARA SETAR EM UMA LABEL
vBg = "#ff0" # cor de fundo
vFg = "#000" # cor do texto
vTxt = "Uma Label Mostra Texto!" # texto da label
# criando a label com as configurações resumidas, a escrita de cada configuração foi reduzida para as siglas
txt2 = Label(app_teste,text=vTxt,bg=vBg,fg=vFg)

# PODE-SE CONFIGURAR A POSIÇÃO DA LABEL NO SEU COMPONENTE PAI OU AONDE A LABEL VAI FICAR DENTRO DE QUALQUER OUTRO WIDGET USANDO O PACK, ELE DA MAIS OPÇÃO DE CONFIGURAÇÃO! O PACK E USADA MAIS QUANDO A LABEL VAI DENTRO DE UMA CONTEINER! ELE DA MAIS OPÇÃO DE CONFIGURAÇÃO!
# outra maneira de posicioanar um elemento quando se tem conteiner, posso ajustar o elemento dentro do conteiner
# ipadx(espaçamento interno horizontal dentro da label)
# ipady(espaçamento intern vertical dentro da label)
# padx(espaçamento externo ao redor da label na horizontal)
# pady(espaçamento externo vertical ao redor da label por fora dela)
# side(onde a label deve se posionar dentro do conteiner que ela esta) - #top,right,left,botton - cima,direita,esquerda,baixo
# fill(e a maneira como a label vai ser preenchida dentro do conteiner pode se colocar opções X - prenechimento na horizontal ou Y - preenchimento na vertical)
# se o expand estiver ativo o componente o widget fica expansivel ao conteiner se o conteiner crescer ele , se diminuir ele diminui, fica redimensionado automaticamente redimensiona de acordo com o prenhimento escolhido no Fill
txt2.pack(ipadx=20,ipady=9,padx=30,side="top",fill=X,expand=True)




# executando a janela
# sintaxe
# nomeObjetoJanela.função() 
app_teste.mainloop()

