from model import *
from controller import*

c1 = Categoria('Hortifruti','Frutas legumes e verduras, produtos da horta e do pomar')

lista_compras = [{'Repolho':4},{'Chocolate':2},{'Amaciante':1},{'Sabão em pó':2}]
venda = Venda(lista_compras,datetime.now().strftime('%d/%m/%Y'),'Matheus','Mariana')

VendaDao.efetuar_venda(venda)
VendaDao.ler()
