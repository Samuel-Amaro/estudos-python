# TRABALHANDCO COM CLASSES, ORIENTAÇÃO A OBJETOS;
# HOJE TRABALHANDO COM O CONCEITO DE HERANÇA

# OQUE E HERANÇA EM POO ?: E UMA CLASSE QUE HERDA CARACTERISTICAS DE OUTRA CLASSE. EXISTE UMA CLASSE PAI COM CARACTERISTICAS E METODOS, E EXISTE UMA CLASSE FILHO, NA HERANÇA A CLASSE FILHO HERDA TUDO DA CLASSE PAI, CARACTERISTICAS E METODOS DA CLASSE PAI, SÃO PASSADOS PARA A CLASSE FILHO

# CLASSE BASE, CLASSE PAI OU SUPER CLASSE
class NPC:
    def __init__(self,nome,time,forca,municao): #costrutor
                 self.nome = nome
                 self.time = time
                 self.forca = forca
                 self.municao = municao
    def getInfo(self): #metodo que retorna os dados da propria classe
        print('Nome...: {}'.format(self.nome))
        print('Time...: {}'.format(self.time))
        print('Forca..: {}'.format(self.forca))
        print('Municao: {}'.format(self.municao))

# SINTAXE DE COMO FAZER UMA CLASSE HERDA OUTRA CLASSE:
"""
class nome_classe(classe_pai):
      def __init__(self,parametros): # se tiver um cotrutor na classe filha, esse costrutor sobrescreve o cotrutor da classe pai
"""

# CRIANDO UMA HERANÇA ENTRE AS CLASSE NPC E SOLDADO. CLASSE SOLDADO HERDA TUDO DE NPC
class Soldado(NPC):
     def __init__(self,nome,time):
         self.municao = 200
         self.forca = 50
         # CHAMANDO O COSTRUTOR DA CLASSE PAI, passando paramentros para ele
         super().__init__(nome,time,self.municao,self.forca)  
     # metodo super, serve para invocar e chamar um metodo da classe pai, ou uma propriedade, ele chama qualquer coisa da classe pai, para funcionar na classe filha
     def infoSoldado(self): # vai mostrar dados de um soldado
         super().getInfo() # chamo metodo info da classe pai, e executa na classe filha


# CRIANDO UM OBJETO SOLDADO
s1 = Soldado('Soldado 24','Flamengo')
s1.infoSoldado()