import re #biblioteca Regex para trabalahr com as expressões regulares

# COMO TRABALHAR COM EXPRESSOES REGULARES NO PYTHON
# EXPRESSÕES REGULARES TEM RECURSOS MUITOS INTERESSANTES PARA TRABALHAR COM STRINGS

# FINDALL: SERVE PARA ENCONTRAR TODAS AS OCORRENCIA DE UMA DETERMINADA STRING DENTRO DE OUTRA STRING. E RETORNA UMA COLEÇÃO COM TODAS AS OCORRENCIAS ENCONTRADAS.

texto = "Curso de Python do CFB Cursos, canal do You Tube, conteudo de qualidade e ensino ditatico para quem tem base"

# quero encontrar a string python dentro do meu texto acima
# usa função re.findall(string_procura_ou_letra,onde_procurar_string) return uma coletion

resultado = re.findall("Python",texto)

# como saber a quantidade de ocorrencias que o findall encontrou
# a função coletion.count() vai contar a quantidade de vezes que o item  informado por paramentro esta na coletion
quantidade_ocorrencia = resultado.count("Python")

print(str(resultado) + " qtd: " + str(quantidade_ocorrencia))


