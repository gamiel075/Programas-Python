class Transação:

    #high-level banking transactions

    list_transaction = []

    def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date):
        self.__id = id
        self.__account_sender = account_sender
        self.__recipients_account = recipients_account
        self.__balance_sent = balance_sent
        self.__shipping_date = shipping_date
        self.list_transaction.append(self)

    def rate(self):
        return self.__balance_sent * 0.05
    

class person_to_company(Transação):

    def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date,product_context):
        super().__init__(id,account_sender,recipients_account,balance_sent,shipping_date)
        self.__proproduct_contextn = product_context

    def rate(self):
        return self.__balance_sent * 0.1
    
    class person_to_person(Transação):

        def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date):
            super().__init__(id,account_sender,recipients_account,balance_sent,shipping_date)

        def rate(self):
            return self.__balance_sent * 0.05
        
class company_to_company(Transação):

    def __init__(self,id,account_sender,recipients_account,balance_sent,shipping_date):
        super().__init__(id,account_sender,recipients_account,balance_sent,shipping_date)

    def rate(self):
        return self.__balance_sent * 0.20
    

class profit():
    def __init__(self,profit_management = 0):
        self._profit_management = profit_management

    def registre(self,profit_management):
        if(isinstance(profit_management,Transação)):
            self._profit_management += profit_management
        else:
            print('o obj add {} não tem implementaçao aqui'.format(self.__class__.__name__))

    @property
    def profit_management(self):
        return self._profit_management
    
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





            
        

        




        
        

        

    
    





    


