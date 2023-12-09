#dashboard

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from colorama import Fore, Back, Style, init




def quadro_lojas():
    print('---' * 30)
    x = 1
    faturamento = 0

    for x in range(1,8):
        faturamento1 = float(input('valor do faturamento da loja {}'.format(x)))
        faturamento += faturamento1

    print('---' * 30)
    receita = float(input('digite a receita final'))
    Despesas = float(input('digite as depesas'))
    lucro = receita - Despesas
    print(faturamento)
    print('---' * 30)

    return faturamento , receita , Despesas , lucro

    
    #grafico de barras aqui
    

def quadro_lojas2(faturamento,receita,Despesas,lucro):
    
    Médiaxloja = faturamento / 7
    Déficit = faturamento - receita
    mediaxhora = faturamento / 276
    print(Despesas)
    print(lucro)
    return Médiaxloja , mediaxhora


def quadro_lojas3(faturamento,receita,Despesas,lucro):
    import matplotlib.pyplot as plt
     # Dados em uma lista
    rótulos = ['Faturamento', 'Receitas', 'lucro' , 'Despesas']
    valores =[faturamento , receita,Despesas,lucro]

#cores,no caso a penas a barra 'faturamento' nesse caso vc ira adcionar mais um componente
    cores = ['red','blue' ,'blue' , 'blue' ]
# Criar uma figura e eixos
    fig, ax = plt.subplots()

# Criar o gráfico de barras
    ax.bar(rótulos, valores , color = cores)

# Inserir rótulos de dados e título do gráfico
    ax.set_xlabel('Distribuição de valores')
    ax.set_ylabel('Margem')
    ax.set_title('Quadro financeiro')

# Exibir o gráfico
    plt.show()


def quadro_lojas4(Despesas):

    quadro_despesas = []
    for i in range(5):
        titulo = input('digite o nome do titulo')
        valor = float(input('digite o valor'))
        quadro_despesas.append([titulo,valor])
    print('---' * 30)
    print(quadro_despesas)
    print('---' * 30)


    

    if(quadro_despesas[0][1] + quadro_despesas[1][1] + quadro_despesas[2][1] + quadro_despesas[3][1] + quadro_despesas[4][1] > Despesas  ):
        print( 'a inconcistências pendentes' )

    elif(quadro_despesas[0][1] + quadro_despesas[1][1] + quadro_despesas[2][1] + quadro_despesas[3][1] + quadro_despesas[4][1] <  Despesas  ):
        print( 'a inconcistências pendentes,valores em débito não catálogados' )

    elif(quadro_despesas[0][1] + quadro_despesas[1][1] + quadro_despesas[2][1] + quadro_despesas[3][1] + quadro_despesas[4][1] <  Despesas  ):
        print( 'a inconcistências pendentes,valores em débito não catálogados' )

        return quadro_despesas
    


    rotulos = [quadro_despesas[0][0],quadro_despesas[1][0],quadro_despesas[2][0],quadro_despesas[3][0],quadro_despesas[4][0]]
    valores = [quadro_despesas[0][1],quadro_despesas[1][1],quadro_despesas[2][1],quadro_despesas[3][1],quadro_despesas[4][1]]
    cores = ['red','green','blue','yellow','brown']

    fig, ax = plt.subplots()
    ax.pie(valores, labels=rotulos, colors=cores, autopct='%1.1f%%')

    ax.set_title('Distribuição de Débitos')



    plt.show()

def quadro_lojas5(Médiaxloja ,  mediaxhora):

    if(Médiaxloja > 143000 ):
             print(Fore.GREEN + str(Médiaxloja) )

    elif(Médiaxloja < 143000 and Médiaxloja > 135000):
             print(Fore.BLUE + str(Médiaxloja) )

    elif(Médiaxloja <  1350000 and Médiaxloja> 115000):
             print(Fore.YELLOW + str(Médiaxloja) )

    elif(Médiaxloja <  115000 and Médiaxloja > 0 ):
             print(Fore.RED + str(Médiaxloja) )

    if(mediaxhora   > 3625 ):
             print(Fore.GREEN + str(mediaxhora) )

    elif(mediaxhora < 3625 and mediaxhora > 3200):
             print(Fore.BLUE + str(mediaxhora) )

    elif(mediaxhora <  3200 and mediaxhora> 2800):
             print(Fore.YELLOW + str(mediaxhora) )

    elif(mediaxhora <  2800 and mediaxhora > 0 ):
             print(Fore.RED + str(mediaxhora) )


resulta = quadro_lojas()
resultb = quadro_lojas2(*resulta)
resultc = quadro_lojas3(*resulta)
resultd = quadro_lojas4(resulta[2])
resulte = quadro_lojas5(*resultb)
















    


