# CRIANDO UM WIDGET(ELEMENTO VISUAL), BARRA DE MENU;

from tkinter import *

# criando uma janela
janelaPrincipal = Tk()

# dando um titulo para janela
janelaPrincipal.title("BARRA DE MENUS")

#configurando o tamanho da janela
janelaPrincipal.geometry("500x300")

#configurando uma cor de fundo para a janela, as cores são informadas por parametro com represetação em codigo hexadecimal rgb
janelaPrincipal.configure(background="#93A3BA")


# função que se associa a um clique de um botão, da uma ação para um botão
def testeComando():
    print('teste clicou')


# criando um widget de tipo barra de menu, onde os menus fica localizado
# nomeObejto = Menu('componente(widget ou conteiner) pai')
barraDeMenu=Menu(janelaPrincipal)

# criando um widget de tipo menu, ele fica localizado dentro da barra de menu, esse widget menu, e um menu que vai ter varios opções de escolha onde usuario pode escolher oque deseja
# nomeObejtoMenu = Menu('componete barra de menu pai',tearoff=0) #tearoff=0 tira uma linha pontilhada do menu

menu01Contato = Menu(barraDeMenu,tearoff=0)


# criando a primeira opção do menu, opção de criar um novo contato
# nomeObjetoMenu.add_comand(label='nome opção',command='função que ao clicar na opção menu e executada')
menu01Contato.add_command(label="Novo Contato",command=testeComando)
# criando a segunda opção do menu de contato, opção de pesquisar
menu01Contato.add_command(label="Pesquisar",command=testeComando)
# criando a terceira opção do menu de contato, opção de Deletar
menu01Contato.add_command(label="Deletar",command=testeComando)

# criando uma separação visual, criando um elemento widget separator, colocar uma barra de separação na horizontal para ficar visualmente mais bonito
menu01Contato.add_separator()

# criando a Quarta opção do menu de contato, opção de Fechar 
# obs: na opção do comando de associar uma função a opção do menu, e uma função automatica de fechar a janela automaticamente, isso e atraves da janela principal que e o componente pai da barra de menu, tem uma opção de fechar janela automaticamente # obejtoJanela.quit()
menu01Contato.add_command(label="Fechar",command=janelaPrincipal.quit)


# definindo o menu com um elemento visual um efeito drop
# nomeObejto.add_cascade(label='nome menu',menu='nome obejto menu')
barraDeMenu.add_cascade(label="Contatos",menu=menu01Contato)

# add o barra de menu a janela, a barra de menu e add diretamente, sem precisar configurar posicionamento;
# add o widget barra de menu, que ja possui configuração de barra de menu, e menu ja configurado com opções, de menu;
# janela principal recebe a configuração de um menu
# objetoJanela.configure(menu='objeto barra menu')
janelaPrincipal.configure(menu=barraDeMenu)


# CRIANDO MAIS UM MENU, UM MENU DE BANCO DADOS, UM MENU QUE VAI TER OPÇÕES DE BANCO DE DADOS
menuManuntencao = Menu(barraDeMenu,tearoff = 0)

# ADD UMA OPÇÃO AO MENU DE MANUNTENÇÃO  
menuManuntencao.add_command(label="Banco de Dados",command=testeComando)

# ADD O MENU MANUTENÇÃO DE BANCO DE DADOS A BARRA DE MENU
barraDeMenu.add_cascade(label="Manutenção",menu=menuManuntencao)

# CRIANDO MAIS UM MENU, UM MENU DE SOBRE, SOBRE O SISTEMA
sobreSistema = Menu(barraDeMenu,tearoff=0)

# ADD UMA OPÇÃO AO MENU sobreSistema
sobreSistema.add_command(label="Information System",command=testeComando)

# ADD O MENU sobreSistema na barra de menu
barraDeMenu.add_cascade(label="Informação Sistema",menu=sobreSistema)

# executando aplicação grafica e todos componentes
janelaPrincipal.mainloop()