import abc
from tabulate import tabulate

class shopping(abc.ABC):

    def __init__(self,id,buyer,value,date_of_purchase):
        self.__id = id
        self.__buyer = buyer
        self.__value = value
        self.__date_of_purchase = date_of_purchase

    def get_id(self):
        return self.__id
    def get_buyer(self):
        return self.__buyer
    def get_value(self):
        return self.__value
    def get_date(self):
        return self.__date_of_purchase



    @abc.abstractclassmethod
    def consult(self):
        pass

class shopping_foods(shopping):
    def consult(self):
        return self.get_id()

      

    

c1 = shopping_foods(1111,'gabriel',20.25,'01/02/2024')
c2 = shopping_foods(2222, 'ana', 15.50, '05/03/2024')
c3 = shopping_foods(3333, 'carlos', 30.00, '10/04/2024')
c4 = shopping_foods(4444, 'maria', 12.75, '15/05/2024')
c5 = shopping_foods(5555, 'joao', 40.20, '20/06/2024')
c6 = shopping_foods(6666, 'laura', 22.90, '25/07/2024')
c7 = shopping_foods(7777, 'pedro', 18.30, '30/08/2024')
c8 = shopping_foods(8888, 'julia', 10.00, '04/09/2024')
c9 = shopping_foods(9999, 'fernanda', 27.45, '08/10/2024')
c10 = shopping_foods(1010, 'rafael', 35.60, '12/11/2024')

print(c10.consult()) #saida = 1010
