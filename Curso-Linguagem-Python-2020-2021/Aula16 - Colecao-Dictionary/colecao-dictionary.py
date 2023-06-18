# UMA COLEÇÃO DE TIPO DICTIONARY;
# DICTIONARY E O TIPO DE COLETION CHAVE VALOR(KEY VALUE);
# DICTIONARY E UMA COLEÇÃO ABERTA, PODE INSERIR, ALTERAR, REMOVER VALORES, E USAR INDEXAÇÃO;

# CRIANDO UM DICTIONARY: se trabalha com chaves, no modelo chave valor, cada dado, precisa de uma chave e um valor relacionado a essa chave, uma dupla chave valor e um dado na dictionary;
# sintaxe:
"""
nomeDictionary = {
                  'chave':'valor',
                  'chave':'valor',
                   .       .
                   .       .
                   .       .
                 }                      
"""
pessoa = {
         "Nome":"Samuel",
         "idade":"20",
         "fone":"9995-1944"
         }

# como mostrar os valores de uma dictionary
print(pessoa) # mostra tudo

# como mostrar um valor especifico ?
# uso a chave, correspondente do valor, ai mostra valor
nome = pessoa["Nome"]
print(nome)

# ou posso usar um metodo get do proprio dictionary que eu informo uma chave e ele me retorna o valor dessa chave
idade = pessoa.get('idade')
print(idade)

# como adicionar um novo valor atraves de uma chave
# vou mudar o nome da pessoa
pessoa['Nome'] = 'Sineuma'

# mostrando as chaves e valores de uma dictionary atraves de um iteração, indexação

for chave,valor in pessoa.items():
    print(chave + ":" + valor)

# como saber o tamanho de uma dictionary, o tamanho vai ser aa quantidade de conjunto chave valor existente no dicionario
print("Tamanho de uma Dictionary pessoa {}".format(len(pessoa)))

# como remover um conjunto de chave valor no dictionary
# pessoa.pop('chave')

# metodo clear, limpa todo dictionary
# pessoa.clear()

# PODE - SE CRIAR UM DICTIONARY, COM CHAVE E VALOR, SO QUE NO VALOR DE CADA CHAVE VAI SER UMA NOVA DICTIONARY, ASSIM CADA CHAVE VAI REPRESENTAR UMA NOVA DICTIONARY

# para cada chave vai ter como valor um novo dictionary
pessoas = {
            'Pessoa-01': 
            {   
              'Nome':'Samuel',
              'Idade':'20',
              'Peso':'59.90'  
            },
            'Pessoa-02':
            {
              'Nome': 'Abadia',
              'Idade':'48',
              'Peso':'60.0'
            },
            'Pesssoa-03':
            {
              'Nome':'Humberto',
              'Idade':'56',
              'Peso':'89'
            }
         }

# como imprimir esse novo dictionary
print(pessoas['Pessoa-01'])

# imprimindo o valor da chave 01 - e imprimindo o valor da chave 01 dentro da chave 01
print(pessoas['Pessoa-01']['Nome'])

# CRIANDO VARIOS DICTIONARYS

miguel = {
           'cpf':'064.232.731-97',
           'identidade':'000.333.90',
           'status':'Desativado'
         }
prieto = {
          'cpf':'000.321.456-00',
          'identidade':'123.456.78',
          'status':'Ativado'
         }

# na dictionary abaixo vou criar so as chaves porque os valores de cada chave vai ser uma dictionary criada acima
listaBeneficiarios = {
                     'b1':miguel,
                     'b2':prieto
                     }

                     