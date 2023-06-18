#importando a biblioteca json
import json

# COMO TRABALHAR COM JSON NO PYTHON

# COMO CRIAR UM JSON
pessoa_json = '{"Nome":"Mark","CPF":"000.000.000-90","Idade":"15"}'

# como criar uma variavel que vai carregar o json
pessoa = json.loads(pessoa_json)
# o metodo loads(json) tranforma uma varivel, converte ela para string no formato json, a variavel recebi uma string quase no formato de um dictinary, assim pode ser manipulado igual um dicionario

# imprimindo todo dictionary
print(pessoa)

# imprimindo valores de cada chave
print(pessoa["Nome"])

# imprimindo so as chaves do dictionary itera todo dictionary
for chave in pessoa:
    print(chave)

# imprimindo so os valores de cada chave itera todo dictionary
for valor in pessoa.values():
    print(valor)

# imprimindo a chave e o valor correpondente itera todo dictionary
for chaveValor in pessoa.items():
    print(chaveValor)

# CONVERTE UM DICTIONARY PARA UM JSON

# criando um dictionary
pessoa_dic = {
              "Nome":"Mark",
              "CPF":"000.000.000-90",
              "Idade":"15"
              }

# convertendo o dictionary para um json
pessoa_json_02 = json.dumps(pessoa_dic)

# a variavel pessoa_json_02 agora tem um json carregado nela
print(pessoa_json_02)
