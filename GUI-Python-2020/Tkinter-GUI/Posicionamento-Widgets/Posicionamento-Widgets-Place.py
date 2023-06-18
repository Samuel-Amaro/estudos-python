# COMO POSICIONAR WIDGETS USANDO O METODO PLACE

import tkinter as tk

class Tela:
    def __init__(self,nomeTela):
        super().__init__()
        self.tela = nomeTela;
        self.botao = tk.Button(self.tela,text="BOTÃO COM POSICIONAMENTO ABSOLUTO")
        # posicionando o botão dentro da janela
        
        # utilizando o metodo place
        # posicionamento fixo(absoluto) não se move, onde foi posicionado vai permanecer ali
        # self.widget.place(cordenadX,cordenadaY)
        # cordenada x = posicionamento crescente da esquerda para direita na horizontal
        # cordenada y = posicionamento crescente de cima para baixo, na vertical;
        # todo widget com posicionamento absoluto começa sempre no topo superior esquerdo;
        self.botao.place(x=150,y=200)

        self.botao2 = tk.Button(self.tela,text="BOTÃO COM POSICIONAMENTO RELATIVO")

        # POSICIONANDO O BOTÃO 02 
        # APLICANDO O POSICIONAMENTO RELATIVO: e porque o widget vai ser posicionado ao tamanho relativo da tela
        # AS CORDENADAS NÃO SERÃO FIXAS
        # relx = cordenada X relativa (valores aceitos 0.0 ~ 1.0, 0 = 0% , 1 = 100%) - quantos porcento da tela posso utilizar para posicionar o widget na horizontal, em relação a tela
        # rely = cordenada Y relativa (valores aceitos 0.0 ~ 1.0, 0 = 0% , 1 = 100%) - quantos porcento da tela posso utilizar para posicionar o widget na vertical, em relação a tela 
        # self.widget.place(relx=porcentagemRelativaNaCordenadaXQueWidgetVaiSePosicionarNaTela,rely=porcentagemRelativaNaCordenadaYQueWidgetVaiSePosicionarNaTela)
        #opções que podemos aplicar dentro do metodo place que altera a dimensão de um widget 
        # width = largura do widget(largura absoluta)
        # height = altura do widget(altura absoluta)
        # pode-se utilizar a largura e altura relativa em relação ao tamanho da tela
        # relwidth = largura relativa em relação ao tamanho da tela - valores(0.0 ~ 1.0 : 0 = 0% e 1 = 100%)
        # relheight = altura relativa em relaçaõ ao tamanho da tela - valores(0.0 ~ 1.0 : 0 = 0% e 1 = 100%)
        self.botao2.place(relx=0.1,rely=0.5,relwidth=0.3,relheight=0.7)



        
janela = tk.Tk()

Tela(janela)

janela.mainloop()