"""
 # PANED WINDOWS(JANELAS PANORÂMICAS)
  - Um widget de janela panorâmica permite empilhar dois ou mais widgets redimensionáveis ​​acima e abaixo um do outro (ou à esquerda e à direita). 
  - Os usuários podem ajustar as alturas (ou larguras) relativas de cada painel arrastando uma faixa localizada entre eles.
  - Normalmente, os widgets que você está adicionando a uma janela panorâmica serão quadros contendo muitos outros widgets.
  - É importante ressaltar que cada painel adicionado à janela do painel deve ser um filho direto da própria janela do painel.
"""

from tkinter import ttk
from tkinter import *

# criando janela
app = Tk()
app.title("PANED WINDOWS")
app.geometry("500x300")

# criando uma janela panoramica (PANED-WINDOWS)
# tkk.PanedWindow(componentePai,orient)
# orient = pode possui VERTICAL e Uma janela de painel é vertical(seus painéis são empilhados verticalmente uns sobre os outros) ou horizontal
# estilização do widget PanedWindow
# bd = largura da borda
# relief = tipo de borda
# bg = cor de fundo 
# esse e o painel pai de todos, o que agrupa outros paineis
conteiner1 = PanedWindow(bd=4,relief='raised',bg='red')
conteiner1.pack(fill=BOTH,expand=1)

# criando uma label para add dentro do painel
left_label = Label(conteiner1,text="LABEL BARRA DE MENU")
conteiner1.add(left_label)

"""
 - Chamar o add método adiciona um novo painel ao final da lista de painéis. O método permite que você coloque o painel na posição dada na lista de painéis (0..n-1). Se o painel já for gerenciado pela janela panorâmica, ele será movido para a nova posição.
 - Você pode usar o para remover um painel da janela panorâmica (você também pode passar uma posição em vez de uma subjanela).insert position subwindow forget subwindow
"""

# criando outro painel que vai dentro do painel pai, esse painel vai ficar na horizontal dentro do outro painel, esse painel vai ter uma orientação vertical
conteinerHeadTop = PanedWindow(conteiner1,orient=VERTICAL,bd=4,relief='raised',bg='green')
#add o painel 2 dentro do painel 1
conteiner1.add(conteinerHeadTop)

# criando uma lalel para poder ter um elmento grafico dentro do painel 2
labelTop = Label(conteinerHeadTop,text="LABEL CABEÇALHO")
conteinerHeadTop.add(labelTop)

# criando outro painel que vai estar dentro do painel geral
conteinerBotton = Label(conteinerHeadTop,text="LABEL RODAPE")
conteinerHeadTop.add(conteinerBotton)



app.mainloop()