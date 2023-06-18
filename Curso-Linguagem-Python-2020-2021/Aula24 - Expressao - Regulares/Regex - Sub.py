import re #biblioteca para usar as expressões regulares


texto = "Curso de Python, do CFB Cursos, canal do You Tube, conteudo de qualidade e ensino ditatico para quem tem base"

# FUNÇÃO SUB: FAZ SUSBTITUIÇÃO DE STRING POR OUTRA STRING, TROCAR STRING POR STRINGS, CARACTER POR CARACTER, FAZ A SUBSTITUIÇÃO DE STRING; ELA RETORNA A NOVA STRING JA COM CARACTERES SUBSTITUIDOS
# re.sub("oque vai ser substituido","oque_vou_colocar_lugar",onde_esta_string)

print("Antes de substituir \n" + texto)
# quero trocar toda virgula por um ponto final
resultado = re.sub(",",".",texto)
print("Depois de Substituir\n" + resultado)