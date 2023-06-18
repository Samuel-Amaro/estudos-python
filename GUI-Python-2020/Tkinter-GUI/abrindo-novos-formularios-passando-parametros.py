# APRENDER A ABRIR UM  NOVO FORMULARIO COM UM JA ABERTO E PASSANDO PARAMETROS PARA O NOVO FORMULARIO QUE VAI SER ABERTO
# ABRIR UM NOVO FORMULARIO ATRAVES DE UM JA EXISTENTENTE

# importando todos widgets e tudo que preciso para trabalhar com interface grafica no python
from tkinter import *

# istanciando uma nova janela, a principal
janelaPrincipal = Tk()

# dando um titulo para a janela
janelaPrincipal.title("JANELA PRINCIPAL")

# configurando o tamanho da janela
janelaPrincipal.geometry("500x300")

# configurando uma cor de fundo da janela principal
janelaPrincipal.configure(background="#574EF4")

# função que se associa ao botão, ao botão ser clicado essa função vai ser chamada e executada intantaneamente;
# configurando uma ação para o botão ao ser clicado;
# a tarefa que essa função tem que fazer e criar uma nova janela, a nova janela não vai ser criada aqui nesse programa, mas vai abrir outro arquivo.py onde vai possui uma nova janela ja configurada e pronta para ser executada;
def criaNovoFormulario():
    #pode se fazer a tarefa de se abrir um novo formulario a partir de um existente de varias maneiras uma das maneiras e usando o comando exec;
    # exec('comando do sistema que exec recebe para executar');
    # como no caso quero abrir um novo formulario a partir de um existente, vou mandar o exec abrir um novo arquivo.py com um novo formulario criado e configurado para ser aberto;
    # abre um arquivo - open('caminho ate arquivo')
    # metodo read - le os caracteres do arquivo ate o final do arquivo, le todo o arquivo
    # apos o metodo read, posso passar parametros para a janela secundaria que vai ser aberta, parametros que vão ser passados para a nova janela, para o novo formulario que vai ser criado
    caminhoArquivo = "C:\\Users\\SAMUE\\Documents\\Programacao-Cursos-Projetos-2020\\GUI-Python-2020\\Tkinter-GUI"
    exec(open(caminhoArquivo + "\\abrindo-formularios-passando-parametros-parte02.py").read(),{'x':10})

# criando um  botão para a janela, vai ficar dieretamente posicioando na janela sem um conteiner de agrupamento de elementos
btnNovoFormulario = Button(janelaPrincipal,text="Criar Novo Formulario",command=criaNovoFormulario)
btnNovoFormulario.place(x=200,y=130,width=150,height=20)

# executando o programa de interface grafica, chamando a janela o formulario para ser executado
janelaPrincipal.mainloop()
