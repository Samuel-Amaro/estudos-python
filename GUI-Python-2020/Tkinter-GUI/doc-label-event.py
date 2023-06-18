# UM CODIGO QUE MOSTRA COMO UMA LABEL PODE TRATAR DIFERENTES EVENTOS DO MOUSE

from tkinter import * 
from tkinter import ttk 

janela = Tk () 
label = ttk.Label (janela, text = "Iniciando ...") 
label.grid () 
label.bind ('<Enter>', lambda e: label. configure (text = 'Movido mouse para dentro')) 
label.bind ('<Leave>', lambda e: label.configure (text = 'Movido mouse para fora')) 
label.bind ('<1>', lambda e: label.configure (text = 'Botão esquerdo do mouse clicado')) 
label.bind ('<Double-1>', lambda e: label.configure (text = 'Clique duplo')) 
label.bind ('<B3-Motion > ', lambda e: label.configure (text =' botão direito arraste para % d,% d '% (ex,ey))) 

janela.mainloop ()