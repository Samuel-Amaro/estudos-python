"""
 # STRING FORMATAÇÃO
"""
"""
 * SEQUÊNCIAS DE ESCAPE
   - TAMBEM CHAMDOS DE CÓDIGOS DE BARRA INVERTIDA;
   - PERMITEM O ENVIO DE CARACTERES DE CONTROLE NÃO GRAFICOS PARA DISPOTIVOS DE SAIDA
   \n - nova linha
   \t - tabulação
   \v - tabulação vertical
   \b - retrocesso
   \' - aspas simples
   \" - aspas duplas
   \\ - barra invertida

   - SÃO EXECUTDAS SEMPRE QUE A BARRA INVERTIDA É ECONTRADA
   - PARA EVITAR QUE AS SEQUÊNCIAS DE ESCAPE FUNCIONEM, BASTA DEFINIR A STRING COMO UMA ROW STRING

   - PARA ISSO BASTA PRECEDER A STRING COM r ou R
"""
print("Linguagem \\ Python") # executa sequencia de escape
print(r"LInguagem \\ Python") # faz a sequencia de escape não ser executada

"""
 # FORMATAÇÃO DE STRINGS
  
  - TAMBÉM E POSSIVEL FORMATAR STRING COM O OPERADOR %
    - O CONTEUDO DA STRING DA ESQUERDA PRECEDIDO POR UM % É SUBSTITUIDO POR UM VALOR A DIREITA (ENTRE PARENTESES)

  - FORMA GERAL
    - string-a-ser-formatada%(lista-de-valores)  
"""

str = "O reajuste foi de %d %% e a inflação de %.2f %%" % (10,6.5)
print(str)

"""
 # FORMATAÇÃO DE STRINGS
   - NA STRING DA ESQUERDA, O CONJUNTO DE CARACTERES DEPOIS DO % DEFINE O TIPO FORMATAÇÃO A SER EXECUTADA

   %c - caractere
   %s - string
   %d - inteiro
   %u - inteiro sem sinal
   %f - reais ponto flutuante
   %.NF reais com N casas decimais
   %% simbolo de %
"""