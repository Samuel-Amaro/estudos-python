# COMO CRIAR UM WIDGET(ELEMENTO VISUAL) DO TIPO BOTÃO USANDO O TKINTER; 
# COMO FAZER O BOTÃO TER UMA AÇÃO, COMO ASSOCIAR O BOTÃO A UMA FUNCIONALIDADE DENTRO DO PROGRAMA;

from tkinter import *


# obs: os componentes estão sendo posicionados diretmanete dentro de uma janela, sem usar um conteiner de posicionamento, por isso utilizamos o metodo place, porque o ideal e usar o metodo pack com um conteiner de agrupamento de elementos


# criando um objeto de tipo janela
janela = Tk()

#titulo da janela
janela.title("Entrada de Texto")

# tamanho da janela
janela.geometry("400x400")

#cor de fundo da janela
janela.configure(bg="#dde")

#criando uma label nome
lblNome = Label(janela,text="Nome",background="#dde",foreground="#009",anchor=W)
#paramentro anchor(com as indicações cardiais posso indicar em que sentido quero que fique a minha ancora o texto dentro da label) - opções:
#N=Norte,S=Sul,E=Leste,W=Oeste,NE=Nordeste,SE=SUDESTE,SO=Sudoeste,NO=NOROESTE

# dizenodo aonde quero que minha label fique dentro da janela, dando o posicionamento dela
lblNome.place(x=5,y=20,width=200,height=10)

# componente de entrada de texto de uma linha;
#componente que recebe uma entrada de texto de uma linha so, serve para entrada de texto simples de uma so linha sem quebra
#intancia objeto e no costrutor da o seu componente pai
# nomeObjeto = Classe('componente pai')
getNome = Entry(janela)
# posicionamento do Entry dentro da janela
getNome.place(x=5,y=40,width=200,height=20)


# criando uma label telefone
lblTelefone = Label(janela,text="Telefone",background="#dde",foreground="#009",anchor=W)
#posicionamento da label telefone dentro da janela
lblTelefone.place(x=5,y=80,width=200,height=10)

#componente de entrada de texto
#componente que recebe uma entrada de texto de uma linha so, so para texto simples
getTelefone = Entry(janela)
#posicionamento dentro da janela
getTelefone.place(x=5,y=100,width=200,height=20)

#criando uma label email
lblEmail = Label(janela,text="Email",background="#dde",foreground="#009",anchor=W)
# posiscionamento da label email dentro da janela
lblEmail.place(x=5,y=140,width=200,height=10)


#criando um componente de entrada de texto simples so de uma linha
getEmail = Entry(janela)
# posicionamento da caixa de entradada de texto dentro da janela
getEmail.place(x=5,y=160,width=200,height=20)


# criando uma label Obs
lblObs = Label(janela,text="Obs",background="#dde",foreground="#009",anchor=W)
# posicionamento da label dentro da janela
lblObs.place(x=5,y=200,width=200,height=10)


# componente de entrada de texto de varias linhas, pode ser digitada varias linhas dentro dele;
# criando uma caixa de entradada de texto do tipo Text, uma caixa que pode receber um texto com varias linhas, o usuario pode digitar um texto de varias linhas
# componente de multiplas linhas
# objeto = Text('componente pai')
getObs = Text(janela)
# posicionamento do componente dentro da janela
getObs.place(x=5,y=220,width=350,height=100)


# função que vai se associar, ao botão, vai ser a função que vai ser acionada quando  o botão for clicado;
# uma funçaõ que recebe os dados dos componentes de entrada de texto e grava esses dados em um arquivo.txt para mostrar para o usuario;

# criando arquivo no caminho do programa e no modo de anexo, todo novo conteudo vai ser anexado ao final do arquivo
arquivoDados = open("C:\\Users\\SAMUE\\Documents\\Programacao-Cursos-Projetos-2020\\GUI-Python-2020\\Tkinter-GUI\\dadosGravados.txt","a")

def gravaDados():
    # obtendo os dados que os componentes de entrada de texto recebe e mostrando ao usuario, esses dados vem atraves de uma variavel, um obejto que foi instanciado ao criar um componente
    # objeto.get() retorna o texto que ele armazena ao receber uma entrada de texto do usuario
    # %s(recebe um texto vindo de uma variavel ou obejto)
    # % associa uma variavel ou obejto a um caracter de formatação de saida, mostrando o texto

    #escrevendo dados no arquivo, usando função write, os dados escritos vem  dos objetos de entrada de texto
    arquivoDados.write("Nome....: %s" % getNome.get() + "\n")
    arquivoDados.write("Email...: %s" % getEmail.get() + "\n")
    arquivoDados.write("Telefone: %s" % getTelefone.get() + "\n")
    # quando o componente de entrada de texto e um componete que pode recener varias linhas, para obter a entrada de texto tem que informar um intervalo em que quer o texto, no caso abaixo quero da linha 1 ate o final;
    # mas pode informar um intervalo com indices para obter so um pedaço do texto, informa onde começa,onde termina
    arquivoDados.write("Obs.....: %s" % getObs.get(1.0,END) + "\n\n")
    # fechando arquivo e salvando alterações no arquivo
    arquivoDados.close()
    
    print('Bem Vindo, Você Clicou no Botão!')


#CRIANDO UM COMPONENTE DE BOTÃO
# CRIANDO UM WIDGET DE TIPO BOTÃO
# nomeObjeto = Button('componente pai',text='texto que vai aparecer no botão',command='função que deve ser executada quando o botão for clicado')
btnImprimir = Button(janela,text='Gravar',command=gravaDados)
# executando programa(aplicação grafica com as janelas e tudo)
# posicionamento do botão dentro da janela
btnImprimir.place(x=120,y=340,width=100,height=20)



janela.mainloop()