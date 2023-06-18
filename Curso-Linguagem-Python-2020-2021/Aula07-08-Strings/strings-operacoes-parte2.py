# OPERAÇÕES E MANIPULAÇÃO DE STRINGS PARTE 02 - AULA 08

frase = "Estou aprendendo uma nova Linguagem de Programação"

# PALAVRAS CHAVES (IN e NOT IN) A PALAVRA IN(RELACIONADA A STRING, VAI VERIFICAR SE POSSUI UMA VARIAVEL(STRING) ou uma chave de tipo String, dentro de uma String), e NOT IN(verifica se em uma string não existe uma palavra ou variavel informada de tipo string em uma outra string(variavel ou objeto))

# EXEMPLO 01 - VERIFICA SE NA STRING FRASE POSSUI A PALAVRA (nova), USANDO A PALAVRA CHAVE IN(esta), se tiver retorna true, se não tiver retorna false
"""    (palavra ou variavel) esta na (variavel ou objeto de tipo String informada)"""
respostaIn = "nova" in frase
print("Palavra (nova) esta na Variavel Frase ? "); print(respostaIn)

# EXEMPLO 02 - VERIFICA SE A PALAVRA (nova) não esta NA VARIAVEL FRASE, USANDO AS PALAVRAS CHAVE NOT IN(não esta), RETORNA TRUE OU FALSE
"""     (palavra ou variavel) não esta na (variavel ou objeto, de tipo String) ?"""
respostaNotIn = "nova" not in frase
print("Palavra (nova) não esta na Variavel Frase ? "); print(respostaNotIn)

# CONCATENAÇÃO DE STRINGS EM PYTHON

# EXEMPLO 01
nome = "Samuel"
sobrenome = "Amaro"
nomeCompleto = nome + " " +  sobrenome
print(nomeCompleto)

# COMO CONCATENAR DIFERENETES TIPOS DE DADOS EM UMA SAIDA SEM PRECISAR FAZER UM CAST USANDO O format()

cidade = "Formosa"
dia = 24
mes = "Julho"
ano = 2020
information = "{}, {} de {} de {}"
print(information.format(cidade,dia,mes,ano)) # os paramentros do format(as variavies), vão substituir os plays({}) rouders na variavel data, seguindo a mesma sequencia da formatação, seguindo a formatação que criei na variavel

