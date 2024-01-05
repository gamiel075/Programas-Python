import pandas as pd
import xlsxwriter


class PRODUTO:
    list_produtos = []

    def __init__(self,id,nome_produto,preço_produto,tipo_produto,qtd_produto):
        self._id = id
        self._nome_produto = nome_produto
        self._preço_produto = preço_produto
        self._tipo_produto =  tipo_produto
        self._qtd_produto = qtd_produto
        self.list_produtos.append(self)


    def promoção(self):
        return self._preço_produto * 0.15
    
    def get_id(self):
        return self._id

    def get_name(self):
        return self._nome_produto

    def get_preço_produto(self):
        return self._preço_produto

    def get_tipo_produto(self):
        return self._tipo_produto
    
    def get_qtd_produto(self):
        return self._qtd_produto

    @classmethod
    def create_dataframe(cls):
        data = []
        for Produtos_obj in cls.list_produtos:
            produtos_data = {
            'id':Produtos_obj.get_id(),
            'nome':Produtos_obj.get_name(),
            'preço':Produtos_obj.get_preço_produto(),
            'tipo':Produtos_obj.get_tipo_produto(),
            'qtd':Produtos_obj.get_qtd_produto()
            }

            data.append(produtos_data)

        df  =  pd.DataFrame(data)
        df.to_excel('data_mercado.xlsx' , index =  False)
        print(df)

class bebidas(PRODUTO):
    def __init__(self,id,nome_produto,preço_produto,tipo_produto,qtd_produto,tipo_bebida,litro_bebida):
        super().__init__(id,nome_produto,preço_produto,tipo_produto,qtd_produto)
        self._tipo_bebida =  tipo_bebida
        self._litros_bebida = litro_bebida

    def promoção(self):
        return self._preço_produto * 0.20
    
class frutas(PRODUTO):
    def __init__(self,id,nome_produto,preço_produto,tipo_produto,qtd_produto,qtd_pacote,kilos):
        super().__init__(id,nome_produto,preço_produto,tipo_produto,qtd_produto)
        self._qtd_pacote = qtd_pacote
        self._kilos = kilos

    def promoção(self):
        return self._preço_produto * 0.25
    
class carnes(PRODUTO):
    def __init__ (self,id,nome_produto,preço_produto,tipo_produto,qtd_produto,kilos_carne):
        super().__init__(id,nome_produto,preço_produto,tipo_produto,qtd_produto)
        self._kilos_carne = kilos_carne

class Roupas:
    def __init__(self,nome):
        self._nome =nome


class gestão_promoção():
    def __init__(self,gestão_promoção = 0):
        self._gestão_promoção = gestão_promoção

    def registre(self,produtos):
        if(isinstance(produtos,PRODUTO)):
            self._gestão_promoção += produtos.promoção()
        else:
            print('o obj add {} não tem implementaçao aqui'.format(self.__class__.__name__))

    @property
    def gestão_promoção(self):
        return self._gestão_promoção
    


#M'p0 = bebidas(id,nome do produto,preço produto,tipo produto,qtd do produto no estoque,tipo de bebida, litro)
p1 = bebidas(111,'coca- cola',10,'bebida',10,'refrigerante',2)
p1 = bebidas(111, 'Coca-Cola', 10, 'bebida', 10, 'refrigerante', 2)
p2 = bebidas(222, 'Guaraná', 7.5, 'bebida', 15, 'refrigerante', 2)
p3 = bebidas(333, 'Água Mineral', 3.5, 'bebida', 30, 'água', 1.5)
p4 = bebidas(444, 'Suco de Laranja', 8.99, 'bebida', 12, 'suco', 1)
p5 = bebidas(555, 'Cerveja', 15.99, 'bebida alcoólica', 24, 'cerveja', 0.5)
p6 = bebidas(666, 'Vinho Tinto', 25.99, 'bebida alcoólica', 8, 'vinho', 0.75)
p7 = bebidas(777, 'Chá Gelado', 6.5, 'bebida', 18, 'chá', 1.5)
p8 = bebidas(888, 'Energético', 12.99, 'bebida', 7, 'energético', 0.25)
p9 = bebidas(999, 'Leite', 4.75, 'bebida', 22, 'láctea', 1)

#po = frutas(id,nome do produto,preço produto,tipo produto,qtd do produto no estoque,quanridade de itens no pacote,kilos do produto ou gramas)
p10 = frutas(1111,'tomate',2,'frutas',20,5,0.215)
p12 = frutas(1113, 'Banana', 2.5, 'frutas', 30, 7, 0.18)
p13 = frutas(1114, 'Laranja', 2.8, 'frutas', 25, 5, 0.3)
p14 = frutas(1115, 'Abacaxi', 4, 'frutas', 18, 4, 1.5)
p15 = frutas(1116, 'Morango', 5.5, 'frutas', 22, 8, 0.1)
p16 = frutas(1117, 'Uva', 6, 'frutas', 20, 9, 0.15)
p17 = frutas(1118, 'Pera', 3.5, 'frutas', 28, 6, 0.35)
p18 = frutas(1119, 'Manga', 4.2, 'frutas', 24, 5, 0.22)
p19 = frutas(1120, 'Kiwi', 4.8, 'frutas', 26, 4, 0.12)
p20 = frutas(1121, 'Melancia', 7, 'frutas', 16, 3, 4)
p21 = frutas(1122, 'Pêssego', 4.5, 'frutas', 29, 7, 0.25)

#po = frutas(id,nome do produto,preço produto,tipo produto,qtd do produto no estoque,kilos de carne no pacote)
p22 = carnes(222,'Alcem',20,'carnes',30,5)
p23 = carnes(223, 'Bife de Fraldinha', 25, 'carnes', 25, 4)
p24 = carnes(224, 'Coxa de Frango', 15, 'carnes', 35, 3)
p25 = carnes(225, 'Costela Bovina', 30, 'carnes', 20, 6)
p26 = carnes(226, 'Filé Mignon', 40, 'carnes', 18, 2)
p27 = carnes(227, 'Picanha', 50, 'carnes', 22, 3.5)
p28 = carnes(228, 'Linguiça Toscana', 18, 'carnes', 28, 1.5)
p29 = carnes(229, 'Salmão', 35, 'carnes', 15, 2)
p30 = carnes(230, 'Cordeiro', 45, 'carnes', 17, 3)
p31 = carnes(231, 'Peito de Peru', 30, 'carnes', 26, 3.5)

PRODUTO.create_dataframe()
gestão = gestão_promoção()
gestão.registre(p1)
gestão.registre(p12)
gestão.registre(p23)
print(gestão.gestão_promoção)
#saida: 6.375

p32= Roupas('camisa vermelha')
gestão.registre(p32)














