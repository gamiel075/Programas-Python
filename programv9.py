class Transação:

    #high-level banking transactions
    #atenção os atributos não estão privados para melhor estudo.
    #attention the attributes are not private for better study.

    list_transaction = []

    def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date):
        self._id = id
        self._account_sender = account_sender
        self._recipients_account = recipients_account
        self._balance_sent = balance_sent
        self._shipping_date = shipping_date
        self.list_transaction.append(self)

    def get_id(self):
        return self._id

    def get_account(self):
        return self._account_sender

    def get_recipients_account(self):
        return self._recipients_account

    def rate(self):
        return self._balance_sent * 0.05
    

class person_to_company(Transação):

    def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date,product_context):
        super().__init__(id,account_sender,recipients_account,balance_sent,shipping_date)
        self._proproduct_contextn = product_context

    def rate(self):
        return self._balance_sent * 0.1
    
class person_to_person(Transação):

    def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date):
        super().__init__(id,account_sender,recipients_account,balance_sent,shipping_date)
        self._balance_sent = balance_sent
        #name mangling (resolução para conflito de nomes)

    def rate(self):


        if(self._balance_sent > 25000):
            return self._balance_sent  * 0.05
        
        elif(self._balance_sent > 15000 and  self._balance_sent < 25000):
            return self._balance_sent * 0.04

        elif(self._balance_sent > 10000 and  self._balance_sent < 15000):
            return self._balance_sent * 0.03

        
class company_to_company(Transação):

    def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date):
        super().__init__(id,account_sender,recipients_account,balance_sent,shipping_date)

    def rate(self):
        return self._balance_sent * 0.20

   
    
class bank:

    def __init__(self,id,transactions):
        self.id = id
        self.transactions = transactions

    def __getitem__(self,item):
        return self.transactions[item]
    
    def __len__(self):
        return len(self.transactions)
    
    def listagem(self):
        print(self.transactions)
    
    def tamanho(self):
        print(len(self.transactions))

    def add_item(self,item):
        self.transactions.append(item)

class profit():
    def __init__(self,profit_management = 0):
        self._profit_management = profit_management

    def registre(self,profit_management):
        if(isinstance(profit_management,Transação)):
            self._profit_management += profit_management.rate()
        else:
            print('o obj add {} não tem implementaçao aqui'.format(self.__class__.__name__))
    
    @property
    def profit_management(self):
        return self._profit_management

    #id,cliente(fisico),empresa(destinário),valor enviaado,data de envio,contexto se é compra ou venda

t1 = person_to_company(1111,'gabriel','nike',2000,'01/03/2025','compra')
t2 = person_to_company(1112,'miguel','apple',2850,'01/02/2025','pagamento de fatura')
t3 = person_to_company(1113,'rafael','positivo',3150,'04/03/2025','investimento')
t4 = person_to_company(1114,'daniel','lg',3150,'04/03/2025','devolução')
t5 = person_to_company(1115, 'Sophia', 'Samsung', 2500, '05/03/2025', 'compra')
t6 = person_to_company(1116, 'Isabella', 'Microsoft', 3000, '06/03/2025', 'pagamento de fatura')
t7 = person_to_company(1117, 'Luis', 'Sony', 2800, '07/03/2025', 'investimento')
t8 = person_to_company(1118, 'Gabriel', 'Dell', 3200, '08/03/2025', 'devolução')
t9 = person_to_company(1119, 'Miguel', 'HP', 2700, '09/03/2025', 'compra')
t10 = person_to_company(1120, 'Rafael', 'Lenovo', 3300, '10/03/2025', 'pagamento de fatura')
t11 = person_to_company(1121, 'Daniel', 'Acer', 3100, '11/03/2025', 'investimento')
t12 = person_to_company(1122, 'Lucas', 'Asus', 3400, '12/03/2025', 'devolução')
t13 = person_to_person(1123,'jhon','mike',17623,'12/03/2025')
t14 = person_to_person(1124,'willian','igor',25365,'08/03/2025')
t15 = person_to_person(1125, 'Paula', 'Carla', 18900, '15/03/2025')
t16 = person_to_person(1126, 'Matheus', 'Bruno', 20200, '18/03/2025')
t17 = person_to_person(1127, 'Fernanda', 'Camila', 21500, '21/03/2025')
t18 = person_to_person(1128, 'Gustavo', 'Eduardo', 22800, '24/03/2025')
t19 = person_to_person(1129, 'Marina', 'Amanda', 24100, '27/03/2025')
t20 = person_to_person(1130, 'Thiago', 'Lucas', 25400, '30/03/2025')
t21 = person_to_person(1131, 'Luiza', 'Isabela', 26700, '02/04/2025')
t22 = person_to_person(1132, 'Pedro', 'Henrique', 28000, '05/04/2025')
t23 = person_to_company(1133,'mercado livre','Nestlê',1500000,'05/04/2025','compra')
t24 = person_to_company(1134,'amazon','redhat',2389445,'24/03/2025','investimento')
t25 = person_to_company(1135, 'Alibaba', 'Google', 1875000, '15/04/2025', 'compra')
t26 = person_to_company(1136, 'eBay', 'IBM', 2149000, '18/04/2025', 'pagamento de fatura')
t27 = person_to_company(1137, 'Walmart', 'Oracle', 2250000, '21/04/2025', 'investimento')
t28 = person_to_company(1138, 'Alibaba', 'Microsoft', 2325000, '24/04/2025', 'devolução')
t29 = person_to_company(1139, 'Amazon', 'Intel', 2475000, '27/04/2025', 'compra')
t30 = person_to_company(1140, 'Mercado Livre', 'AMD', 2550000, '30/04/2025', 'pagamento de fatura')
t31 = person_to_company(1141, 'Magalu', 'NVIDIA', 2600000, '03/05/2025', 'investimento')

balance = profit()
balance.registre(t1)
balance.registre(t15)
balance.registre(t26)
print(balance.profit_management)
#saida:215856.0

list_transfer = [ t1,t2,t3,t4,t5,t6,t7]
banK = bank('transfer_bank',list_transfer)
banK.listagem()

for g in banK:
    print(g.get_id())
    #saida:1111,1112,1113,1114,1115,1116,1117

print(len(banK)) 
#saida = 7

  

 



            
        

        




        
        

        

    
    





    


