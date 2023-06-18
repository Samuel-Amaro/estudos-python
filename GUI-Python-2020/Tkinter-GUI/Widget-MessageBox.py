# WIDGET - MESSAGEBOX - CAIXAS DE MENSAGEM

from tkinter import *
# importando o modulo que trabalha com  as caixas de mensagens do tkinter
from tkinter import messagebox

# criando uma janela principal
app = Tk()
app.title("CAIXAS DE MENSAGEM")
app.geometry("500x400")
app.configure(background="#1C585C")

# função que recebe parametros para poder mostrar um tipo de mansagem, e de acordo com o tipo de mensagem vai ter a caiax de mensagem especifica, isso e a função vai poder trabalahr com os 3 tipos de caixa de mensagem que existe
def mostraMensagem(tipoMensagem,mensagem):
        # cx de mensagem de tipo informação
        if(tipoMensagem == "1"):
            # trabalalhando com as caixas de mensagem
            # criando uma caixa de mensagem do tipo infomação
            # sintaxe:
            # messagebox.showinfo(title='titulo da caixa de mensagem',message='mensagem que de informação que vai aparecer')
            messagebox.showinfo(title="INFORMAÇÃO",message=mensagem)
        elif(tipoMensagem == "2"):
            # caixa de mensagem de alerta warnig
            messagebox.showwarning(title="AVISO/ALERTA",message=mensagem)
        elif(tipoMensagem == "3"):
            # caixa de mensagem de tipo error, quando se trata de mostra que algo no programa dei errado
            messagebox.showerror(title="ERRO/DEU-RUIM",message=mensagem)


# CRIANDO UMA LABEL QUE VAI MOSTRA UMA INFORMAÇÃO PARA O USUARIO
lblMensagem = Label(app,text="ESCOLHA UMA OPÇÃO ABAIXO PARA CAIXA DE MENSAGEM DE TIPO INFORMAÇÃO")
# posicionamento da label dentro da janela e sua altura e largura
lblMensagem.place(x=15,y=20,width=470,height=20)

# variavel que armazena os valores de opçõa escolhida pelo usuario no option menu
# o usuario escolheu uma opção eu coleto o valor dessa opção escolhida atraves dessa variavel
valorOpcaoOptionMenu = StringVar()

# coletion - tipo list que mostra as opções do menu
opcoesCaixaMensagem = ["1","2","3"]

# criando um option menu para mostrar as opções que o usuario pode escolher para mostar um certo tipo de caixa de mensagem
opCaixasMensagem = OptionMenu(app,valorOpcaoOptionMenu,*opcoesCaixaMensagem)
# posicionando o option menu dentro da janela e configurando largura e altura do option menu
opCaixasMensagem.place(x=150,y=60,width=200,height=30)

# criando uma label para mostra uma mensagem para o usuario
lblMensagemEntrada = Label(app,text="DIGITE A MENSAGEM ABAIXO")
# configurando posicionamento do label dentro da janela e sua altura e largura
lblMensagemEntrada.place(x=150,y=110,width=200,height=20)


# criando uma caixa de texto para receber uma entrada de texto do usuario para colcocar uma mensagem, na caixa de mensagem 
txtMensagemUser = Entry(app)
# posicionando a caixa de entrada de texto de um linha so, e config largura e altura dela
txtMensagemUser.place(x=75,y=150,width=350,height=25)


# criando um botão que vai possuir a tarefa de ao ser clicado mostra a caixa de mensagem que o usuario escolheu e mostra a mensagem que o usuario digitou para ser mostrada na caixa
# PARA ADICIONAR UMA FUNÇÃO AO COMAMAND UMA FUNÇÃO QUE RECEBA PARARAMETROS TEM QUE USAR UMA LAMBDA, PORQUE AI A LAMBDA CHAMA A FUNÇÃO E PASSA OS PARAMETROS NÃO O BOTÃO DIRETAMENTE
btnMostraCxMensagem = Button(app,text="MOSTRAR CAIXA",command=lambda:mostraMensagem(valorOpcaoOptionMenu.get(),txtMensagemUser.get()))
# posicionando o botão dentro da janela e configurando altura e largura da caixa
btnMostraCxMensagem.place(x=75,y=195,width=100,height=20)

# OUTROS TIPOS DE CAIXA DE MENSAGEM - CAIXAS DE MENSAGEM DE ITERAÇÃO COM O USUARIO
def limpaCampos():
    # caixa de mensagem de tipo pergunta com 2 botões sim e não
    # botõa sim pussui valor = True
    # botão não possui valor = False
    # nenhume botão clicado = None
    resultadoCxMensagem = messagebox.askyesno("LIMPAR","DESEJA LIMPAR MENSAGEM ?")
    if(resultadoCxMensagem == True):
       # limpa toda a entrada de texto digitada pelo usuario 
       txtMensagemUser.delete(0,END)  
 
# criando uma botão que vai possuir a tarefa de limpar os campos no formulario e mostra as caixas de mensagem de iteração para o usuario
bntLimpar = Button(app,text="LIMPAR MENSAGEM",command=limpaCampos)
# posicionando o botão na janela principal, dando config de largura e altura
bntLimpar.place(x=195,y=195,width=130,height=20)


# FUNÇÃO QUR VAI MOSTRAR AS CAIXAS DE ITERAÇÃO QUE EXISTE, SÃO CAIXAS EM QUE O USUARIO INTERAGE ATRAVES DE BOTÕES
def cxIteracao(tipoCx):
    if(tipoCx == "1"):
       # caixa de tipo (pergunte sim não) - botões sim(valor True) e não(Valor false)
        resultadoCxMensagem = messagebox.askyesno("CAIXA MENSAGEM PERGUNTA","AQUI VAI A PERGUNTA")
    elif(tipoCx == "2"):
        # caixa de tipo askquestion(faz pergunta) - botões sim(valor true) e não(valor false) 
        resultadoCxMensagem = messagebox.askquestion("CAIXA DE TIPO PERGUNTA","AQUI VAI SUA PERGUNTA AO USUARIO")
    elif(tipoCx == "3"):
        # caixa de tipo askokcancel(pergunte ok cancelar) - botões ok(valor true) e cancel(valor false)
        resultadoCxMensagem = messagebox.askokcancel("CAIXA DE PERGUNTA","AQUI VAI SUA PERGUNTA")
    elif(tipoCx == "4"):
        # caixa de tipo askretrycancel(pedir tente cancelar) - botões REPETIR(valor true) e CANCELAR(valor false)
        resultadoCxMensagem = messagebox.askretrycancel("CAIXA PEDIR","AQUI VAI SEU PEDIDO")
    elif(tipoCx == "5"):
        # caixa de tipo askyesnocancel(pergunte sim não cancele) - botões SIM(valor True) e não(valor false) e Cancel(valor None)
        resultadoCxMensagem = messagebox.askyesnocancel("CAIXA PERGUNTA","AQUI VAI SUA PERGUNTA")

# mostrando uma label de informação
lblInformation = Label(app,text="ESCOLHA O TIPO DE CAIXA MENSAGEM DE ITERAÇÃO ABAIXO")
# configurando e posicionando a label na janela
lblInformation.place(x=60,y=235,width=380,height=20)
        
# criando uma coletion de tipo list que vai mostra as opções do menu 
listCxMs = ["1","2","3","4","5"]

# variavel que vai receber o valor de cada opção escolhida para
getValorOp = StringVar()
getValorOp.set("1")

# criando um option menu que vai mostrar as opções de caixa de mensagem de tipo iteração para o usuario escolher e navegar e ver cada uma delas
opCx = OptionMenu(app,getValorOp,*listCxMs)
# posisicionando o option menu na janela
opCx.place(x=225,y=275,width=50,height=20)


# botão que vai ter a terefa de mostrar a respectiva caixa de mensagem escolhida pelo usuario no option menu
btnCx = Button(app,text="MOSTRAR CAIXA",command=lambda:cxIteracao(getValorOp.get()))
# posicionando o botão
btnCx.place(x=200,y=315,width=100,height=20)


# executando programa 
app.mainloop()