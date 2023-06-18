# AULA 12 - LOOPS NO PYTHON - EXISTE DUAS ESTRUTURA DE REPETIÇÃO NO PYTHON
# FOR e WHILE
# Loop FOR(para percorrer coleções, iterar array);
# Loop WHILE(Repetir de fato uma estrutura, um comando, ou um bloco de comando);

# CRIANDO UMA COLEÇÃO TIPO ARRAY(LIST)
carros = ["GOLG5","FIAT TORO","CAMARO","LOGAM","FORD KA","FIT","HILUX"]

# UTILIZANDO UM LOOP FOR PARA PERCORRE UMA LIST
# SINTAXE
# FOR variavel(recebe cada item da coleção usada) in coleçãoQueEstaUsando:
  # execute esses comandos a cada iteração de item na coleção
# cada elemento(item) da coleção carros e adicionado na variavel  

print("\nIterando uma coleção \n")
for variavel in carros:
    print(variavel)

# EXEMPLO 02 DE ITERAÇÃO DE ELEMENTOS: POSSO PERCORRER UMA STRING USANDO UM FOR, PORQUE UMA STRING E INDEXAVEL

print('\nIterando uma String\n')
for variavel in "Samuel Amaro":
    print(variavel)    

# EXEMPLO 03 - ENCERRANDO UMA ITERAÇÃO DO FOR,(do loop) QUANDO CHEGAR EM UM ELEMENTO OU CONDIÇÃO QUE EU CRIAR USANDO O COMANDO (BREAK)

print('\nEncerrando uma Iteração do For\n')
for variavel in carros:
   print(variavel)
   if variavel == carros[5]:
       break
