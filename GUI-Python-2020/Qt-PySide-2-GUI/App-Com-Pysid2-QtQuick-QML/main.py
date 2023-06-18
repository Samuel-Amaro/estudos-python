# Seu primeiro aplicativo usando PySide2 e QtQuick / QML 

# todo programa grafico baseado em qt tendo 0 uma ou varias janelas precisa dessa importação
from PySide2.QtWidgets import QApplication 
#(PySide2.QtQuick) - Fornece classes para embutir Qt Quick em aplicações (Qt.QQuickView) - classe fornece uma janela para exibir uma interface de usuário Qt Quick.
from PySide2.QtQuick import QQuickView
# (PySide2.QtCore) - Fornece funcionalidade básica não-GUI. A (QUrl) classe fornece uma interface conveniente para trabalhar com URLs - caminhos de arquivos
from PySide2.QtCore import QUrl

app = QApplication([]) # instancia uma aplicação qt para todo codigo qt conseguir ser executado sem passar nehuma argumento para ele, uma argumento para a aplicação pode mudar o estado dela

# instancia uma tela vazia sem nenhum componente, uma janela de interface de usuario
view = QQuickView() 

# se estiver programando para desktop tem que usar essa linha abaixo
view.setResizeMode(QQuickView.SizeRootObjectToView)

# caminho ate meu arquivo qml que esta desenhando a interface de usuario na linguagem qml
# metodo costrutor Qurl('string com o caminho') # exemplo abaixo no caminho absoluto
# ou pode usar o setUrl('string caminho')
url = QUrl("desenho-tela-qml.qml") 

# Define a fonte para o url, carrega o componente QML e o instancia.
# Certifique-se de que a URL fornecida está completa e correta, em particular, use fromLocalFile()ao carregar um arquivo do sistema de arquivos local.
# pertence a classe QuickView

view.setSource(url) 


 # mostrando a tela para o usuario ja com o qml desenhado nela

view.show()

# executando todo o codigo acima executando toda aplicação
app.exec_()
