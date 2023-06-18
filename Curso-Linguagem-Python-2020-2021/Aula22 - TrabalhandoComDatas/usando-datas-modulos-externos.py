# TRABALHANDO COM DATAS NO PYTHON USANDO MODULOS EXTERNO NO PROGRAMA

import datetime # importando a biblioteca de data

# como saber a data do dia de hoje
data = datetime.datetime.now()
print("Data de Hoje Completa: " + str(data))

# costruindo uma data formatada, pegando paramentros que eu preciso
print(str(data.day) + "/" + str(data.month) +  "/" + str(data.year))

# como criar uma data especifica
nascimento = datetime.datetime(2000,5,2)
print(nascimento)

# opções do srtftime() para formatações de data
"""
%a - dia resumido por extenso
%A - dia completo por extenso
%w - numero do dia da semana se inicia em 0 - 0,1,2,3 - domingo etc..
%d - dia do mes
%b - nome do mes por extexnso resumido
%B - nome do mes por extenso completo
%m - numero do mes
%y - ano com dois digitos
%Y - ano com quatro digitos
%H - hora com dois digitos de 00 - 23
%I - hora com dois digitos de 00 - 12
%p - AM/PM
%M - minutos
%S - segundos
%f - microsegundos
%j - dia do ano se inicia em 0 ate 366
%W - numero da semana do ano
"""