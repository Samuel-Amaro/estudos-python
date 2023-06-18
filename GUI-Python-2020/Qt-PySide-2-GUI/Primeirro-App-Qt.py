# PRIMEIRO APP USANDO O PYSID2 E O QtWidgets 

import sys # modulo que fornece acesso a alguns objetos e funções  e recursos do interpretador
from PySide2.QtWidgets import QApplication, QLabel # importa da subblioteca de PySide 2 as classes Qpll e Q label que vão ser usadas neste programa simples aqui

# cria um novo app uma dialog uma janela
app_teste = QApplication([]) # cria uma intancia. um  objeto da classe Qaplication, cria um obejto da aplicação


# criando uma label
# label pode mostrar textos curtos que tem o poder de mostar um texto simples ou um texto formatado em html ou uma imagem, ou um texto muito rico em formatação
labelMensagem = QLabel("<p text-align=\'center\'>Hello Word!</p>")

# mostrando a label
labelMensagem.show()

# executando a aplicação executa todo codigo qt-criado acima
app_teste.exec_()

