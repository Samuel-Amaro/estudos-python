import re #biblioteca para usar as expressões regulares

# FUNÇÃO SEARCH 
# re.search('oque quero pesquisar','onde deve pesquisar') 
# retorna a posição da primeira ocorrencia que ele encontra, retorna o indice da ocoorencia que ele encontrou, retorna o indice de inicio da ocorencia e o indice do final de onde a ocorrencia termina, retorna o intervalo de indice onde a ocorrencia se encontra

texto = "Curso de Python do CFB Cursos, canal do You Tube, conteudo de qualidade e ensino ditatico para quem tem base"

resultado_pesquisa = re.search("base",texto)

# mostra o resultdao completo, o intervalo de indice e oque mandei procurar
print(resultado_pesquisa)

# como formatar a saida
# variavel_resultado.star() indice inicio
# variavel_resultado.end() indice final
print("Ocorrencia se inicia em: " + str(resultado_pesquisa.start()))
print("Ocorrencia se finaliza em: " + str(resultado_pesquisa.end()))

# como saber o tamanho da ocorrencia
inicio = resultado_pesquisa.start()
final =  resultado_pesquisa.end()
tamanho = final - inicio
print("Tamanho da ocorencia: " + str(tamanho))
