# MOSTRANDO COMO CRIAR UM BOTÃO SIMPLES E APRENDER USAR SINAIS E SLOTS DE BOTÕES DO QT PARA PYTHON
# Sinais e slots é um recurso do Qt que permite que seus widgets gráficos se comuniquem com outros widgets gráficos ou com seu código Python

#  Nosso aplicativo cria um botão que registra o botão clicado, Olá! mensagem para o console Python cada vez que você clica nele.

# importando as bibliotecas necessarias

# Este módulo fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador e a funções que interagem fortemente com o interpretador.
import sys
# (PySide2.QtWidgets) - Estende Qt GUI com funcionalidade de widget C ++. A (QApplication) - classe gerencia o fluxo de controle do aplicativo GUI e as configurações principais. O (QPushButtonwidget) -  fornece um botão de comando
from PySide2.QtWidgets import QApplication,QPushButton
# PySide2.QtCore - Fornece funcionalidade básica não-GUI. classe slot - O novo sinal e estilo de slot do PyQt5 utiliza nomes de método e decorador específicos para sua implementação.
from PySide2.QtCore import Slot
# PySide2 - Estende QtCore com funcionalidade GUI. A QIcon classe fornece ícones escalonáveis ​​em diferentes modos e estados
from PySide2.QtGui import QIcon


# função que da uma saudação para o usuario
# FUNÇÃO QUE DA UMA MENSAGEM DE OLA PARA O USUARIO QUE CLICAR NO BOTÃO A MENSAGEM APARECERA NO CONSOLE
@Slot() #e um decorador que indentifica uma função como um slot
def mensagem():
    print("Parabens Voçê Clicou no Botão, ola!")

# criando a minha aplicação para rodar meu codigo PySide2
# a aplicação so roda se intanciar esse obejto e colocar ele para executar no final do programa

app = QApplication(sys.argv)

# criando um botão atraves da classse QpushButton, criando um obejto botão
# no costrutor do objeto botão e onde se passa um texto, um rotulo para o botão, para o botão mostrar uma mensagem, ou uma frase palavra etc.. para o usuario ver
botao = QPushButton("Clique Aqui!")

#adicionando um icone ao botão
#caminho ate o icone
caminhoIcone = "C:\\Users\\SAMUE\\Documents\\Programacao-Cursos-Projetos-2020\\Curso-Material-GUI-Python-2020-Pysid2\\Botao-Simples\\icones\\icone-botao.png"
# setIcone('objeto da classe QIcon')
# QIcon('arquivo') - cria um icone simples
botao.setIcon(QIcon(caminhoIcone))

# agora vou definir uma ação para o botão, conectando o botão a função mensagem que crie no codigo lencima
# a classe QPushButton possui um sinal predefinido denominado clicked - que é acionado toda vez que o botão é clicado. conectando esse sinal a função mensagem, assim quando usuario clicar no botão mostro uma mensagem para ele atraves da função; atraves do sinal clicado e da função conecte que da a ação para o botão consigo mandar o botão fazer algo
botao.clicked.connect(mensagem)

# mostrando o botão para o usuario
botao.show()

# excutando o app
app.exec_()