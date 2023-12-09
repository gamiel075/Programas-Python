def a():

    faturamento= float(input('digite o registro da arrecadação das vendas'))
    receita = float(input('digite o valor de suas receitas'))
    lucro = float(input('digite o valor final de seu lucro'))
    defice = faturamento - receita
    despesas = receita - lucro
    
    from tabulate import tabulate
    from colorama import Fore, Back, Style, init



    init(autoreset=True)

    

    def get_color(column_name,value,value_to_compare):


         if (column_name == "faturamento"):
            if(faturamento > 1200000 and faturamento < 10000000):
                return Fore.GREEN + str(value)
            
            elif(faturamento < 1200000 and faturamento > 850000):
                return Fore.BLUE + str(value)
            
            elif(faturamento < 850000 and  faturamento> 750000):
                return Fore.YELLOW + str(value)
            
            elif(faturamento < 750000 and faturamento > 0):
                return Fore.RED + str(value)
            
    
    
         elif (column_name == "receita"):
            if( receita > 800000 and receita < 10000000):
                return Fore.GREEN + str(value)
            
            elif(receita < 800000 and receita > 700000):
                return Fore.BLUE + str(value)
            
            elif(receita < 700000 and  receita> 550000):
                return Fore.YELLOW + str(value)
            
            elif(receita < 550000 and receita > 0):
                return Fore.RED + str(value)
            

    
         elif (column_name == "lucro"):
            if( lucro > 600000 and lucro < 10000000):
                return Fore.GREEN + str(value)
            
            elif(lucro < 600000 and lucro > 450000):
                return Fore.BLUE + str(value)
            
            elif(lucro < 450000 and  lucro> 350000):
                return Fore.YELLOW + str(value)
            
            elif(lucro < 350000 and lucro > 0):
                return Fore.RED + str(value)
            
         return  str(value)
    

      
    dados = [
        ['faturamento', get_color('faturamento', faturamento, faturamento)],
        ['receita', get_color('receita', receita, receita)],
        ['lucro', get_color('lucro', lucro, lucro)]]



    # Aplicar a função get_color apenas à coluna 'Valor'
    for linha in dados:
        if linha[0] == 'Valor':
            linha[1] = get_color(linha[1], linha[0])

    tabela_formatada = tabulate(dados, headers=["Indicador", "Valor"], tablefmt="fancy_grid")
    print('---' * 30)
    print(tabela_formatada)
    print('¨¨¨¨¨¨' * 40)
    print('o valor das despesas é: {}'.format(despesas))
    print('o valor di defíce neste mês é {}'.format(defice))
    print('¨¨¨¨¨¨' * 40)




    return faturamento,receita,lucro,despesas
    
  





def b(faturamento,receita,lucro,despesas):
    
    import matplotlib.pyplot as plt
    import matplotlib.pyplot as plt

# Dados
    rotulos = ['faturamento', 'receita', 'lucro', 'despesa' ]
    tamanhos = [faturamento, receita, lucro,despesas]
    cores = ['green', 'blue', 'yellow', 'red']

# Criar figura e eixos
    fig, ax = plt.subplots()

# Criar um gráfico de pizza
    ax.pie(tamanhos, labels=rotulos, colors=cores, autopct='%1.1f%%')

# Adicionar título
    ax.set_title('Balanceamento financeiro')

# Mostrar o gráfico plotado
    plt.show()

result= a()
b(*result)


#o grafico acima na faz sentido