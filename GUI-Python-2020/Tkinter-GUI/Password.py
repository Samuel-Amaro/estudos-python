# WIDGET PASSWORD - SENHA
# CAIXA DE TEXTO DE INSERIR SENHA, MAS QUE NÃO MOSTRE A SENHA PURA, TENHA UMA MASCARA DE DIGITOS PARA NÃO MOSTRAR A SENHA
# não exite um widget do tipo password, tem que adaptar o widget entry para ele se tornar um tipo passaword


from tkinter import *

# criando uma janela
app = Tk()
app.title("CAIXA PASSWORD")
app.geometry("500x300")

# varivel que armazena o resultado de uma caixa de texto, de um input de text
vSenha = StringVar()

# criando uma caixa de text, uma input text, uma caixa de texto onde usuario digita uma entrada de texto, so que vai ser adaptado para se torna um caixa de tipo password, em que o usuario não veja a senha que ele esteja digitando
# usando a configuração show: vai mostrar oque eu define, ao inves de mostrar oque o  usuario digita, ao inves de mostrar o texto digitado, mostra o *, para cada caractere digitado
inputSenha = Entry(app,textvariable=vSenha,show="*")
# posicionando o comoponente na janela
inputSenha.pack()


# função que da uma ação para o botão ao ele ser clicado
def impSenha():
    print("Senha Digitada: " + vSenha.get())
    vSenha.set("texte de inicioa")

# criando um botão
btnMostrarSenha=Button(app,text="Imprimir senha",command=impSenha)
#posicionando o botão na janela
btnMostrarSenha.pack()

app.mainloop()
