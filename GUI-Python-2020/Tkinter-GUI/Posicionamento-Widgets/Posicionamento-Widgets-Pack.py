# POSICIONAMENTO DE WIDGETS
# COM O METODO PACK
# quando se utiliza o pack todos os widgets são empacotados em blocos, um embaixo do outro, e depois são posicionados no widget pai
# padx = margens externas no sentido horizontal
# pady = margens externas no sentido vertical
# ipadx = margens internas no sentido horizontal
# ipady = margens internas no sentido vertical
# todas as margens recebem valores em pixels
# side = define uma direção em que o widget vai se posiconar (Valores = TOP(TOPO),BOTTOM(baixo),RIGHT(DIREITA),LEFT(ESQUERDA))
# fill = essa opção e para prencher ou ocupar um eixo do WIDGET pai, pode dizer para OCUPAR O ESPAÇO DOS EIXOS EM X(HORIZONTAL),Y(VERTICAL),BOTH(AMBOS OS EIXOS) 

import tkinter as tk


class Tela:
    def __init__(self,nome):
        super().__init__()
        self.nomeTela = nome;
        #self.widget = tkNomeDoWidget(self.widgetPai,opcoesDeConfiguração);
        self.lbl = tk.Label(self.nomeTela,text="PRIMEIRA LABEL",background="red")
        self.lbl["font"] = ["Verdana","18"]
        # posicionando a label criada acima, com o metodo pack
        # aplicando uma configuração de margem externa na label no sentido vertical
        # maegen externa e da borda da label para fora
        # POSICIONADA: ESQUERDA
        # se expande na vertical junto com a janela
        self.lbl.pack(pady=20,side=tk.LEFT,fill=tk.Y)
        self.lbl2 = tk.Label(self.nomeTela,text="PRIMEIRA LABEL",background="blue")
        self.lbl2["font"] = ["Verdana","18"]
        # aplicando margens internas na label, nos dois sentidos, margen interna e entre o conteudo e a borda do widget
        # POSICIONADA: A DIREITA
        self.lbl2.pack(ipadx=25,ipady=10,side=tk.RIGHT)
        # CRIANDO 3 LABEL
        self.lbl3 = tk.Label(self.nomeTela,text="PRIMEIRA LABEL",background="blue")
        self.lbl3["font"] = ["Verdana","18"]
        # POSICIONANDO A 3 LABEL NO EIXO DO COMPONETE PAI USANDO O METODO PACK E OPÇÃO FILL
        # se expande na horizontal junto com a janela
        self.lbl3.pack(fill = tk.X)
app = tk.Tk()
Tela(app)
app.mainloop()        