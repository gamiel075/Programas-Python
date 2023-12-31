import pandas as pd
import xlsxwriter
from colorama import Fore, Style
import os



class People:

    number_of_users = 0
    user_aproved = 0
    user_denied = 0
    under_analysis = 0
    list_of_users = []
    __slots__ = ['id', 'name', '__password', 'city', '_value', '_squad', '_status']



    def __init__(self,id,name,password,city,_value,_squad):

        self.id = id
        self.name = name
        self.__password = password
        self.city = city
        self._value = _value
        self._squad = _squad
        People.number_of_users += 1

        if(self._value > 10000):
            self._status = 'alfa'
            People.user_aproved += 1


        elif(self._value > 5000 and self._value <10000):
            self._status = 'beta'
            People.user_denied += 1 

        
        elif(self._value > 0 and self._value < 5000 ):
            self._status = 'shallow'
            People.under_analysis += 1


    
    @property
    def get_squad(self):
        return self._squad
    
    @get_squad.setter
    def set_squad(self, new_squad):
        q5 = float(input('Digite a senha: '))
        if q5 == self.__password:
            self._squad = new_squad
        else:
            print('Acesso negado')

    @property
    def get_value(self):
        return self._value
        
    @get_value.setter
    def set_value(self, new_value):
        q1 = float(input('Digite a senha para alteração'))
        if q1 == self.__password:
             self._value = new_value
        else:
            print('Autenticação não autorizada')

    @classmethod
    def create_dataframe(cls):

        q2 = float(input('digit password of admin'))
        if(q2 == 67890):

            data = []
            for people_obj in cls.list_of_users:
                people_data = {
                    'id': people_obj.id,
                    'name':people_obj.name,
                    'city':people_obj.city,
                    'value':people_obj._value,
                    'squad':people_obj._squad
                }
                data.append(people_data)


            df = pd.DataFrame(data)
            df.to_excel('dados_lojas.xlsx', index =False)
            print(df)

        else:
            print('acess negate')

    @classmethod
    def consult_admin(cls):

        q5 = float((input('digit password')))
        if(q5 == 67890):


            print('total number users')
            print(People.number_of_users)
            print('----' * 10)
            print('total user aprooved')
            print(People.user_aproved)
            print('----' * 10)
            print('total user denied')
            print(People.user_denied)
            print('----' * 10)
            print('total under analysis')
            print(People.under_analysis)


        else:
            print('acess negate')

    

    def consult(self):

        q4 = float((input('digit password')))
        if(q4 == self.__password):

            if(self._status == 'alfa'):

                print('---' * 10)
                print(self.name)
                print(self._value)
                
            #acessvip
            elif(self._status == 'beta'):
                print('---' * 10)
                print(self.name)
                print(self._value)
        
            elif(self._status == 'shallow'):
                print('---' * 10)
                print(self.name)
                print(self._value)

        else:
            print('acess negate')

   
    

p1 = People(111,'Carlos',267,'São Paulo',15020,'wolfs')
p2 = People(222,'maria',211,'Rio de Janeiro',2030,'lions')
p3 = People(333,'joao',771,'Belo Horizonte',7530,'tigers')
p4 = People(444,'camila',256,'Porto Alegre',3694,'birds')
p5 = People(555, 'Fernanda', 555, 'Curitiba', 5550, 'wolfs')
p6 = People(666, 'Pedro', 666, 'Salvador', 6066, 'lions')
p7 = People(777, 'Aline', 777, 'Florianópolis', 7077, 'tigers')
p8 = People(888, 'Ricardo', 888, 'Recife', 888, 'birds')
p9 = People(999, 'Mariana', 999, 'Campinas', 999, 'wolfs')
p10 = People(1010, 'Roberto', 1010, 'Fortaleza', 1010, 'lions')
p11 = People(1111, 'Ana', 1111, 'Manaus', 1111, 'tigers')
p12 = People(1212, 'Paulo', 1212, 'Belém', 1212, 'birds')
p13 = People(1313, 'Amanda', 1313, 'Porto Velho', 1313, 'wolfs')
p14 = People(1414, 'Lucas', 1414, 'Vitória', 1414, 'lions')
p15 = People(1515, 'Pedro', 1515, 'Rio de Janeiro', 1515, 'tigers')

admin = People.consult_admin()
admin2 = People.create_dataframe()




















    



    

        
        










            







        





    
