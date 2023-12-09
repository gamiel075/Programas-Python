

#uma copia deste programa está no diretório Programas Phyntom

import pandas as pd

class Viagem:

    def __init__(self,distancia_km,preço_gasolinalocal, velocidade_viagem,tipo_carro):

        self.distancia_km = distancia_km
        self.preço_gasolina_local = preço_gasolinalocal
        self.velocidade_viagem = velocidade_viagem
        self.tipo_carro = tipo_carro


    def processar(self):

        eficiencia_energética =0

        print('eficiencia energética é igual á KM/L')

        if(self.tipo_carro == "a"):
           eficiencia_energética += 15

        elif(self.tipo_carro == "b"):
           eficiencia_energética += 10.5
 
        elif(self.tipo_carro == "c"):
           eficiencia_energética += 5.5

        gasto_gasolina = self.distancia_km / eficiencia_energética
        gasto_valor = gasto_gasolina * self.preço_gasolina_local
        gasto_tempo = self.distancia_km / self.velocidade_viagem

        return gasto_gasolina,gasto_valor,gasto_tempo
    
    def mostrar(self,gasto_gasolina,gasto_valor,gasto_tempo):

        dados = [
            ['distancia total',self.distancia_km],
            ['L de gasolina necessário',gasto_gasolina],
            ['R$ gasto em gasolina',gasto_valor],
            ['tempo de viagem em horas',gasto_tempo]
        ]
    
        df= pd.DataFrame(dados)
        df_rounded = df.round(2)
        print(df_rounded)


minhaviagem = Viagem(120,5.60,30,"b")
print(type(minhaviagem))

result=minhaviagem.processar()
minhaviagem.mostrar(*result)


        
    


         



        

        
        
    
        
        
        


         
