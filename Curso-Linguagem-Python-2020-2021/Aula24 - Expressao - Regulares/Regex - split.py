import re #biblioteca para usar as expressões regulares

# FUNÇÃO SPLIT: COMO DIVIDIR UMA STRING E COMO RETORNAR OS ELEMENTOS DIVIDOS EM UMA COLEÇÃO

texto = "Curso de Python do CFB Cursos, canal do You Tube, conteudo de qualidade e ensino ditatico para quem tem base"

# FUNÇÃO SPLIT
# re.split('caracter_que_vai_Ser_o_criterio_de_divisão',onde_procurar_a_string_para_dividir)
# como informo o criterio da função split: pode informar o caracter em si ou um caracter de escape como \s,\n,\t
# retorna uma list coletion list com todas as divisões possiveis feita pelo split


# quero dividir as string que possuem letra a 
resultado_split = re.split('a',texto)

#posso acessar a list, indexadamente
for txt in resultado_split:
    print(txt)

#imprimindo a lista toda    
print(resultado_split)