"""
 * ERROS E EXCEÇÕES

   - Até agora mensagens de erro foram apenas mencionadas, mas se você testou os exemplos, talvez tenha esbarrado em algumas. Existem pelo menos dois tipos distintos de erros: erros de sintaxe e exceções.

 * ERROS DE SINTAXE:

    - Erros de sintaxe, também conhecidos como erros de parse, são provavelmente os mais frequentes entre aqueles que ainda estão aprendendo Python:
"""

# exemeplo de erro de sintaxe

while True print("Hello Word");

"""
  - O parser repete a linha inválida e apresenta uma pequena ‘seta’ apontando para o ponto da linha em que o erro foi detectado. O erro é causado (ou ao menos detectado) pelo símbolo que precede a seta: no exemplo, o erro foi detectado na função print(), uma vez que um dois-pontos (':') está faltando antes dela. O nome de arquivo e número de linha são exibidos para que você possa rastrear o erro no texto do script.
"""
