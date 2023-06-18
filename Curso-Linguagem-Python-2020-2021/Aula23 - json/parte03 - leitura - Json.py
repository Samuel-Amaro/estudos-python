import json

# COMO FAZER A LEITURA DE UM ARQUIVO .JSON PARA SER USADO EM NOSSO PROGRAMA

# CARREGANDO O DOCUMENTO JSON EXTERNO PARA DENTRO DO MEU PROGRAMA
# IMFORMO O CAMINHO ATE ELE, USO O METODO LOAD PARA FAZER O CARREGAMENO DO ARQUIVO E ATRIBUO O RESULTADO EM UMA VARIAVEL QUE VAI RECEBER O JSON CARREGADO PARA O PROGRAMA

with open('C:/Users/SAMUE/Documents/Programacao-Cursos-Projetos-2020/Curso-Linguagem-Python-2020/Aula23 - json/FileJson.json') as JsonExterno: FileJson = json.load(JsonExterno) 

# TESTANDO PARA VER SE DEU CERTO

# MOSTRANDO AS CHAVES DO JSON
for chave in FileJson:
    print(chave)
print("-----------------------------------------------------------")
# MOSTRANDO VALORES DAS CHAVES
for valor in FileJson.values():
    print(valor)
print("-----------------------------------------------------------")
#mostrando itens do json
for itens in FileJson.items():
    print(itens)