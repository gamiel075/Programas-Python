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
    __slots__ = ['id','name','password','city','value','squad']

    def __init__(self,id,name,password,city,value,squad):

        self.id = id
        self.name = name
        self.__password = password
        self.city = city
        self._value = value
        self.squad = squad

        if(self._value > 100000):
            self._status = 'alfa'

        elif(self._value < 100000 and self._value > 50000):
            self._status = 'beta'
        
        elif(self._value < 50000 and self._value > 0 ):
            self._status = 'shallow'

        People.number_of_users += 1

        if(self._status == 'alfa'):
            People.user_aproved += 1

        elif(self._status == 'beta'):
            People.user_denied += 1 

        elif(self._status == 'shallow'):
            People.under_analysis += 1

        self.list_of_users.append(self)

    @property
    def value(self):
        return self._value
        
    value.setter
    def value(self,new_value):
        q1 = float(input('digit password fot alteration'))
        if(q1 == self.__password):
             self._value = new_value
            
        else:
            print('autenthicaton no authorized')

    @classmethod
    def create_dataframe(cls):

        q2 = float(input('digit password of admin'))
        if(q2 == 67890):

            data = []
            for people_obj in cls.list_of_users:
                people_data = {
                    'id': people_obj.id,
                    'name':people_obj.Name,
                    'city':people_obj.city,
                    'value':people_obj.value,
                    'squad':people_obj.squad
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
            print('total user aprooved')
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

    def getsquad(self):
        return self.squad

    def setsquad(self,new_squad):
        q5 = float((input('digit password')))
        if(q5 == self.__password):
            self._value = new_squad
        else:
            print('acess negate')
    
    squad = property(fget = getsquad,fset = setsquad)














    



    

        
        










            







        





    
