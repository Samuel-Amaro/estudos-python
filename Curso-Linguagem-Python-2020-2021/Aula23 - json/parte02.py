import json #biblioteca que usamos para trabalhar com json


# COLETIONS MAIS POPULARES NO PYTHON QUE PODE SER CONVERTIDAS PARA JSON
# UM ELEMENTO EM PYTHON SENDO CONVERTIDO PARA JSON


# DICTIONATY
dictionary_pessoa = {'Nome':'Samuel',
                     'Idade':12,
                     'Peso':59.98,
                     'Cidade':'Formosa'
                     }
# UM DICTIONATY CONVERTIDO PARA JSON VIRA UM OBJETO JSON
# dictionary -> objeto json


# LIST
list_nomes = ['Mikel','Tim','Bianca','Bob','Jonhson']
# LIST CONVERTIDO PARA JSON VIRA UMA LIST JSON
# lits -> array json

# TUPLA
tupla_moto = ('Pop 110i','CG 160 Start','CB 1000R','XJ6')
# tupla -> array json


# PODEMOS FORMATAR A SAIDA DO JSON, ISSO E AO CONVERTER O ELEMENTO PYTHON EM JSON, PODEMOS FORMATAR O JSON CONVERTIDO, PODEMOS FORMATAR OS ELEMENTOS DO JSON
# EXEMPLO: convertendo o dictionary em json e formatando ele para ter uma indentação de 4 caracteres de espaço, trocar o : para o =, e as chaves quero ordenadas em ordem  alfabetica
                                           # indetanção,separador,ordenação
pessoa_json = json.dumps(dictionary_pessoa,indent=4,separators=(":","="),sort_keys=True)

print('Mostrando o Json Formatado Abaixo')
print(pessoa_json)