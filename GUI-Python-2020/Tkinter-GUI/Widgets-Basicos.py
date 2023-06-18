# WIDGETS(ELEMENTOS VISUAIS) MAIS BASICOS DO TKINTER

from tkinter import *
from tkinter import ttk # elementos mais modernos do tkinter

# criando uma janela principal
janelaPrincipal = Tk()

# dando um titulo para janela
janelaPrincipal.title("WIDGETS BASICOS")

#dando uma tamanho para janela
janelaPrincipal.geometry("800x600")

# dando uma cor de fundo para a janela
janelaPrincipal.configure(background="#5F7543")


# widgets basicos do tkinter


# 1 - widget
# frame(quadro ou armação) - serve com um conteiner para agrupar elementos
conteiner = ttk.Frame(janelaPrincipal)
# posicionamento do conteiner dentro da janela
conteiner.place(x=20,y=20,width=200,height=200)
# dando um espaço interno ao conteiner, um padding
conteiner['padding'] = (10,10,10,10)
# dando uma borda para o conteiner. um espaço externo do conteiner para fora
conteiner['borderwidth'] = 2 # 0 == padrão sem borda
# mudando a aparencia visual da borda
conteiner['relief'] = 'sunken' #opções: flat,raised,sunken,solid,ridge,groove



# 2 - widget
# Label(rotulo) - exibe texto ou imagens, que o usuario so visualiza e não interage
labelTxt = ttk.Label(janelaPrincipal,text="Isso e uma Label")
# configurando o posicionamento da label dentro da janela principal, o tamanho de largura e altura da labela
labelTxt.place(x = 240,y=123,width=200,height=20)
# como fazer a label mostrar um texto dinamico, isso e mudo o texto mas não preciso mudar o componente que mostra o texto
txtVariavel = StringVar(janelaPrincipal)
labelTxt['textvariable'] = txtVariavel
txtVariavel.set('Novo texto inserido na label')
# um label que mostra imagem 
labelImagen = ttk.Label(janelaPrincipal,text="Label que Mostra imagen e texto")
# configurando o posicionamento da label na janela e taamnho dela para receber a imagem, label esta com largura e altura no tamanho da imagem e mais um pouco para receber texto
labelImagen.place(x=460,y=98,width=188,height=148)
# recebendo imagen, esta na mesma pasta que o nosso programa python
imagen = PhotoImage(file='imagen-label.png')
# MOSTRANDO IMAGEN NA LABEL
labelImagen['image'] = imagen
# add um texto junto da imagen dentro da label, uma label com texto e imagen
# opção top = imagen acima do texto outras opções #none(mostra apenas imagen se tiver), text(mostra apenas texto),textvariable(mostra apenas conteudo de uma variavel texto),image(mostra apenas imagen se tiver), center(texto no centro da imagen), lef(esquerda),button(inferior baixo),rigth(direita)
labelImagen['compound'] = 'top'



# 3 WIDGET
# botão - (BUTTON) compoente para o usuario interagir emparticular pressionar para executar uma ação
# criando um botao
btn = ttk.Button(janelaPrincipal,text="Um Botão!",command=janelaPrincipal.quit)
# configurando o poscionamento do botão dentro da janela e o seu largura e altura
btn.place(x=30,y=240,width=100,height=30)
# desativando o botão onde usuario não vai poder interagir com o bottão
btn.state(['disabled'])



# 4 - WIDGET
# BOTÃO DE VERIFICAÇÃO - CHECKBUTTON 
# Os botões de verificação são usados ​​o tempo todo quando um usuário é solicitado a escolher entre, por exemplo, dois valores diferentes para uma opção.
# CRIANDO UM BOTÃO DE VERIFICAÇÃO
btnCheck = ttk.Checkbutton(janelaPrincipal,text="Botão de Verificação!",command=janelaPrincipal.quit,onvalue='metric',offvalue='imperial')
# configurando o posicionamento do botão de verificação na janela principal dando largura e altura
btnCheck.place(x=180,y=240,width=150,height=25)



#5 - WIDGET 
# BOTÃO DE RADIO - RADIOBUTTON
# CRIANDO VARIOS BOTÕES DE RADIO, RADIOBUTTON, SE ENCAIXA EM VARIAS OPÇÕES QUANDO SE TEM VARIAS OPÇÕES DE ESCOLHA
#criando um botão de radio com opção 01
btnOpcao01 = ttk.Radiobutton(janelaPrincipal,text='Casa',value='Casa')
# configurando o botão de radio da opção 01 dentro da janela, configurando largura e altura
btnOpcao01.place(x=300,y=280,width=100,height=20)
# criando uma opção de radio button 02
btnOpcao02 = ttk.Radiobutton(janelaPrincipal,text='Escritorio',value='Escritorio')
# posicionamento o radio button de opção 02 dentro da janela
btnOpcao02.place(x=300,y=300,width=100,height=20)
# criando uma opção de radio button 03
btnOpcao03 = ttk.Radiobutton(janelaPrincipal,text='Mobile',value='Mobile')
# posicionamento de radio buton 03 para mostrar dentro da janela principal
btnOpcao03.place(x=300,y=320,width=100,height=20)


# 6 - WIDGET
# ENTRADA DE TEXTO - ENTRY
# UM COMPONENTE EM QUE USUARIO PODE DAR UMA ENTRADA DE TEXTO
txtNome = ttk.Entry(janelaPrincipal)
# posicionando o componente dentro da janela principal
txtNome.place(x=400,y=350,width=200,height=30)
# como deletar um texto dentro da entrada de texto
# txtNome.delete(0,'end') #parametro - começa apagar onde e termina onde
# inseri um texto dentro do campo de texto
# o indice de onde começa e uma linha, cada indice e uma linha
# txtNome.insert(0,'meu nome samuel') #parametro - onde começa a inserir o texto



# campo de texto para senha onde não mostra os caracteres digitados, susbtitui por uma caracter padrão, que vai aparaecer por cada caracter digitado
# show="qualquer carcter para susbtituir os caracteres que irão mostrar a senha"
txtSenha = ttk.Entry(janelaPrincipal,show="#")
# configurando o posicionamento da entrada da senha dentro da janela
txtSenha.place(x=400,y=400,width=200,height=30)




# WIDGET - 6
# CAIXA COMBO - COMBO BOX
cbOpcoes = ttk.Combobox(janelaPrincipal)

#configurando opções para mostrar ao usuario na caixa de escolha
cbOpcoes['values'] = ('java','C','HTML5 e CSS3','PYTHON'  )

#configurando o posicionamento da caixa de comboo box
cbOpcoes.place(x=400,y=470,width=200,height=30)
#saber qual opção da lista de combo box foi escolhida retorna o indice da opção, começa no indice = 0 e vai ate quantas opções tiverem
cbOpcoes.current()




#executando aplicação grafica
janelaPrincipal.mainloop()


