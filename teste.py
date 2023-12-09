


import matplotlib.pyplot as plt

quadro_despesas = [('impostos',50000),('folha de pagamento', 30000),('recomposição',200000)]
despesas = quadro_despesas[0][1] + quadro_despesas[1][1] + quadro_despesas[2][1]

rotulos = [quadro_despesas[0][0],quadro_despesas[1][0],quadro_despesas[2][0]]
valores = [quadro_despesas[0][1],quadro_despesas[1][1],quadro_despesas[2][1]]
cores = ['red','green','blue']

fig, ax = plt.subplots()
ax.pie(valores, labels=rotulos, colors=cores, autopct='%1.1f%%')

ax.set_title('Distribuição de Débitos' + '-total:R$' + str(despesas))




faturamento = 1000000
receita = 800000
despesas = 300000
lucro = receita - despesas 


import matplotlib.pyplot as plt
rótulos = ['Faturamento', 'Receitas', 'lucro' , 'Despesas']
valores =[faturamento , receita,despesas,lucro]

cores = ['red','blue' ,'blue' , 'blue' ]
fig, ax = plt.subplots()

ax.bar(rótulos, valores , color = cores)

ax.set_xlabel('Distribuição de valores')
ax.set_ylabel('Margem')
ax.set_title('Quadro financeiro')


x = 1
faturamento = 0

for x in range(1,8):
    faturamento1 = float(input('valor do faturamento da loja {}'.format(x)))
    faturamento += faturamento1
    
receita = float(input('digite a receita final'))
Despesas = float(input('digite as depesas'))
print(faturamento)



