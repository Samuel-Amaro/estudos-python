# STRINGS E SUAS OPERAÇÕES PARTE 01 - AULA 07

frase = "Estou Aprendendo Linguagem Python"

# OBS: UMA STRING E UM ARRAY DE CARACTERES(LIST QUE ARMAZENA CARACTERES), SENDO UM ARRAY, POSSO USAR O OPERADOR DE INDEXAÇÃO []

# IMPRIMINDO UMA POSIÇÃO DO ARRAY
print(frase[4])

# IMPRIMINDO UM INTERVALO DE CARACTERES DO ARRAY
print(frase[0:5])

# AS LINHAS ABAIXO UTILIZAM FUNÇÕES JA EXISTENTES PARA MANIPULAÇÃO DE STRINGS

# SABENDO O TAMANHO DE UMA STRING(A FUNÇÃO len(string) RETORNA O TAMANHO EM VALOR INT)
print("Tamanho da String: "); print(len(frase))

# FUNÇÃO QUE RETIRA OS ESPAÇOS EM BRANCO DO INICIO E DO FINAL DE UMA STRING strip()
frase2 = " Uma String "
print(frase2)
print(frase2.strip())

# FUNÇÃO QUE CONVERTE UMA STRING PARA CARACTERES MINUSCULOS lower()
frase3 = "Samuel Amaro"
print(frase3)
print(frase3.lower())

# FUNÇÃO QUE CONVERTE UMA STRING TODA PARA CARACTERES MAIUSCULOS upper()
print(frase3.upper())

# FUNÇÃO QUE TROCA UMA PALAVRA OU UM CARACTER DE UMA STRING POR OUTRA PALAVRA OU CARACTER, FAZ A SUBSTITUIÇÃO DE UMA PALAVRA OU CARACTER DENTRO DA STRING POR UMA PALVRA NOVA OU CARACTER NOVO INFORMADO, SUBSTITUI PALVRAS OU CARACTERES OU UMA PROPRIA STRING DENTRO DE UMA STRING função: replace()
print("Frase antiga sem troca: " + frase)
print("Frase nova Com Palavra Trocada: " + frase.replace("Python","C#"))

# FUNÇÃO QUE FAZ UMA SUBDIVISÃO NA STRING, INFORMANDO UM INDICADOR DE ONDE A SUBDIVISÃO DA STRING DEVE OCORRER split(String indicador), sempre que a função split encontrar o indicador ela da um corte na string faz, a divisão da string bem no indicador
frase4 = "Acer Aspire A315-41G-R21B"
print("Função Normal Sem Split: " + frase4)
# quero armazenar o resultado do split
resultSplit = frase4.split(" ") # retorna uma list(Array com as posições indexadas, de cada corte que a string sofreu, isso e retorna a string divida em partes e armazenada indexadamente no array), falei para um split fazer um corte em cada espaço em branco que ele encontrar, quebra a string num indicador
print("Parte 0 da quebra via split: " + resultSplit[0])
print("Parte 1 da quebra via split: " + resultSplit[1])
print("Parte 2 da quebra via split: " + resultSplit[2])
