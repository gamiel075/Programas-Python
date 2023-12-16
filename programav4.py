
class Terminal():

    def __init__(self,user_name,password_user,status_machine,layout):

        self._user_name = user_name
        self._password_user = password_user
        self._status_machine = status_machine
        self._layout = layout


    def login(self):

        while True:

            nome = input('digite seu nome')
            if(nome !=  self._user_name):
                continue

            senha = float(input('digite sua senha'))
            if(senha == self._password_user ):
                print('seja bem vindo')
            
                break

    def acesslayout(self):

        if(self._layout == 'function'):
            pergunta1 = (input('digite o comando desejável'))
            if(pergunta1 == 'checklist'):

                p1 = input('a maquina está limpa?')
                p2 = input('a maquina está carregada?')
                p3 =input('a maquina está limpa?')

            elif(pergunta1 == 'status'):
                if(self._status_machine == False):
                    print('maquina bloqueada')
                        
                
                elif(self._status_machine == True):
                    print('maquina desbloqueada')

                    print('você pode fazer inumeras utilidades,calcular e entre outros bem vindo')




                    
            elif(pergunta1 == 'calcular'):
                    pergunta2=(input('oque voce quer calcular'))


                    if(pergunta2 == 'tabuada'):
                        pergunta3 = float(input('tabuada de que numero'))
                        for x in range(1,11):
                                print(f' {pergunta3} * {x} = {pergunta3 * x}') 
                    
                    elif(pergunta2 == 'somar'):
                        v1 = float(input('digite o primeiro valor'))
                        v2 = float(input('digite o segundo valor'))
                        result = v1 + v2
                        print(f'o resultado de {v1} + {v2} = {result}')

                    
        
        elif(self._layout == 'history'):

            print(self._layout)
            print(self._status_machine)

        elif(self._layout == 'no'):

            print('desculpe mas você não tem permissão para uso')
           

            

    def set_user(self,new_user):

        self._user_name = new_user
        return self._user_name
    
    def get_user(self):
        return self._user_name
    ###########################################
    
    def set_password(self,new_password):

        self._password_user = new_password
        return self._password_user
    
    def get_password(self):
        return self._password_user
    ###########################################
    

    
    def set_status(self,new_status):

        self._status = new_status
        return self._layout
    
    def get_status(self):
        return self._layout
    ###########################################
    
    
    def set_layout(self,new_layout):

        self._layout = new_layout
        return self._layout
    
    def get_layout(self):
        return self._layout
    ###########################################


    
    
usuario_gabriel = Terminal('gabriel',555,False,'history')
new_password = usuario_gabriel.set_password(222)
usuario_gabriel.get_password()
new_status = usuario_gabriel.set_status(True)
usuario_gabriel.get_status
new_layout = usuario_gabriel.set_layout('function')
usuario_gabriel.get_layout
usuario_gabriel.login()
usuario_gabriel.acesslayout()

#usuario_gabriel = Terminal('gabriel',555,False,'history')
#saidas:           #programa não da acesso ao terminal devido a limitalçao inicial

'seja bem vindo'    #isso irá lembrar os comandos chmod de alterar e reduzir permissão  no linux

'history'
'False'



#a partir dos segundos comandos você pode admnistar o uso do programa,lembra quando mexiam com as maquinas e usuarios no mercado livre, então era assim.




                    
        
            
                                  



                    






                    



                        




            




            
            











             
            

            


        


