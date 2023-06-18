"""
 * EXECEÇÕES DEFINIDAS PELO USUARIO

   - Programas podem definir novos tipos de exceções, através da criação de uma nova classe (veja Classes para mais informações sobre classes Python). Exceções devem ser derivadas da classe Exception, direta ou indiretamente.

    - Classes de exceções podem ser definidas para fazer qualquer coisa que qualquer outra classe faz, mas em geral são bem simples, frequentemente oferecendo apenas alguns atributos que fornecem informações sobre o erro que ocorreu. Ao criar um módulo que pode gerar diversos erros, uma prática comum é criar uma classe base para as exceções definidas por aquele módulo, e as classes específicas para cada condição de erro como subclasses dela:
"""

# classe pai que herda exception
class Error(Exception):
    """Classe base para exceções neste módulo.."""
    pass
class ErroEntrada(Error):
    """
       Exceção levantada para erros na entrada.

        Atributos:
            expressão - expressão de entrada em que o erro ocorreu
            mensagem - explicação do erro
    """

    def __init__(self, expressao, mensagem):
        self.expressao = expressao
        self.mensagem = mensagem
    

class ErrorTransicao(Error):
    """
        Levantada quando uma operação tenta uma transição de estado que não é Permitido.

        Atributos:
            anterior - estado no início da transição
            próximo - tentou novo estado
            mensagem - explicação de por que a transição específica não é permitida
    """
    def __init__(self,previos,proximo,mensagem):
        self.preview = previos
        self.proximo = proximo
        self.mensagem = mensagem

"""
  - É comum que novas exceções sejam definidas com nomes terminando em “Error”, semelhante a muitas exceções embutidas.

  - Muitos módulos padrão definem novas exceções para reportar erros que ocorrem no interior das funções que definem. 
"""
