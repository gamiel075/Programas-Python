
from tabulate import tabulate

class documents:
    def __init__(self,id,value,title_type):
        self._id = id
        self._value = value
        self._title_type = title_type

class monthly_payment(documents):
    def m1(self):
        print(self._id)
        

class shopping(documents):
    def m1(self):
        print(self._id)
    

class  invoice(monthly_payment,shopping):
    pass


m1 = monthly_payment(111,2000,'mensalidade')
c1 = shopping(111,355,'compra')
f1 = invoice(111,2355,'fatura')

f1.m1() #saida = 111
m11 = m1._value + m1._value 
print(m11) #saida: 4000


dados = [
    ['id',m1._id],
    ['value', m11],
    ['title',f1._title_type]


]

t = ['id','value','title']
table = tabulate(dados, headers= t , tablefmt='grid')
print(table)
