import pandas as pd
import xlsxwriter



class Rote:

    number_of_rote= 0
    denied_route = 0
    aproved_route = 0
    list_of_rotes = []
    __slots__ = ['id', 'starting_point', 'destin', 'distance', 'time_days', '_load_value', '_status', '__password']




    def __init__(self,id,starting_point,destin,distance,time_days,load_value,status):

        self.id = id
        self.starting_point = starting_point
        self.destin = destin
        self.distance = distance
        self.time_days = time_days
        self._load_value = load_value
        self._status = status
        self.__password = 555
        self.list_of_rotes.append(self)

        Rote.number_of_rote += 1


        if(self._status == True):
            Rote.aproved_route += 1

        elif(self._status == False):
            Rote.denied_route +=1


        
      
    def consult(self):

        risk = 0


        if(self._load_value > 10000):
            risk += 10
        elif(self._load_value < 10000 and self._load_value > 5000):
            risk += 5
        elif(self._load_value < 5000 and self._load_value > 0):
            risk += 0

        print('------------' * 10)
        dados = {'id' : [self.id],
                 'starting point' : [self.starting_point],
                 'destin': [self.destin],
                 'distance' : [self.distance],
                 'time_days' : [self.time_days],
                 'risk':[risk]
                 }
        
        table = pd.DataFrame(dados)
        table.to_csv(f'id{self.id}.csv', index=False)
        print(table)


    @classmethod
    def create_dataframe(cls):
        data = []
        for rote_obj in cls.list_of_rotes:
            rote_data = {
                'id': rote_obj.id,
                'starting point': rote_obj.starting_point,
                'destin': rote_obj.destin,
                'distance': rote_obj.distance,
                'time_days': rote_obj.time_days,
                'load_value': rote_obj._load_value,
                'status': rote_obj._status
            } 
            data.append(rote_data)



        df = pd.DataFrame(data)
        df.to_excel('dados_rotes_novos.xlsx', index=False)
        print(df)


    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self,new_status):
        q1= float(input('digit password'))
        if(q1 == self.__password):
            self._status = new_status
        else:
            print('acess denied')

    def getvalue(self):
        q2 = float(input('digit password'))
        if(q2 == self.__password):
            return self._load_value
        else:
            print('acess negate')

    @staticmethod
    def consult_admin(cls):
        dados = {'routs': [Rote.number_of_rote],
                 'route aproved': [Rote.aproved_route],
                 'route denied': [Rote.denied_route]
                 
                 }
        table2= pd.DataFrame(dados)
        print(table2)
    
   

       

#  def __init__(self,id,starting_point,destin,distance,time_days,load_value,status):

r1 = Rote("r1", "São Paulo", "Rio de Janeiro", 200, 3, 5000, True)
r2 = Rote("r2", "Rio de Janeiro", "Belo Horizonte", 300, 4, 8000, False)
r3 = Rote("r3", "Belo Horizonte", "Brasília", 250, 2, 6000, True)
r4 = Rote("r4", "Brasília", "Salvador", 320, 3, 7500, False)
r5 = Rote("r5", "Salvador", "Fortaleza", 280, 4, 9000, True)
r6 = Rote("r6", "Fortaleza", "Curitiba", 400, 2, 7000, False)
r7 = Rote("r7", "Curitiba", "Manaus", 340, 3, 8200, True)
r8 = Rote("r8", "Manaus", "Belém", 290, 4, 5500, False)
r9 = Rote("r9", "Belém", "Porto Alegre", 380, 2, 6800, True)
r10 = Rote("r10", "Porto Alegre", "São Paulo", 270, 3, 7200, False)
r11 = Rote("r11", "Rio de Janeiro", "Brasília", 310, 4, 6100, True)
r12 = Rote("r12", "Belo Horizonte", "Salvador", 240, 2, 5300, False)
r13 = Rote("r13", "Brasília", "Fortaleza", 330, 3, 8400, True)
r14 = Rote("r14", "Salvador", "Curitiba", 370, 4, 9200, False)
r15 = Rote("r15", "Fortaleza", "Manaus", 260, 2, 6800, True)
r16 = Rote("r16", "Porto Alegre", "Manaus", 500, 5, 10000, True)
r17 = Rote("r17", "Manaus", "São Paulo", 550, 6, 12000, False)
r18 = Rote("r18", "São Paulo", "Belo Horizonte", 600, 4, 8000, True)
r19 = Rote("r19", "Belo Horizonte", "Fortaleza", 450, 7, 13500, False)
r20 = Rote("r20", "Fortaleza", "Salvador", 480, 3, 7200, True)
r21 = Rote("r21", "Salvador", "Brasília", 520, 5, 10400, False)
r22 = Rote("r22", "Brasília", "Curitiba", 540, 6, 10800, True)
r23 = Rote("r23", "Curitiba", "Porto Alegre", 470, 4, 9400, False)
r24 = Rote("r24", "Porto Alegre", "Rio de Janeiro", 510, 3, 10200, True)
r25 = Rote("r25", "Rio de Janeiro", "Belém", 560, 5, 11200, False)
r26 = Rote("r26", "Belém", "Manaus", 530, 4, 10600, True)
r27 = Rote("r27", "Manaus", "Fortaleza", 490, 6, 9800, False)
r28 = Rote("r28", "Fortaleza", "São Paulo", 470, 5, 9400, True)
r29 = Rote("r29", "São Paulo", "Rio de Janeiro", 520, 4, 10400, False)
r30 = Rote("r30", "Rio de Janeiro", "Belo Horizonte", 530, 5, 10600, True)



tabela = Rote.consult(r1)
df_rotes = Rote.create_dataframe()
consult_admin = Rote.consult_admin(r1)
print(dir(Rote))
#vars(r1)

r31 = object.__new__(Rote)
r31.__init__('r31','Rio de Janeiro','Belo Horizonte',550,5,10700,False)
Rote.consult(r31)
print(type(r31))





    
        
        









  
    

    

        

    

    
    
    

    





    

