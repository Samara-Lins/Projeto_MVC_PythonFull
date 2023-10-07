from model import *
from controller import*

c1 = Categoria('Hortifruti','Frutas legumes e verduras, produtos da horta e do pomar')

lista_compras = [{'Tomate':5},{'Leite':12},{'Shampoo':2}]
venda = Venda(lista_compras,datetime.now().strfdatetime('%d/%m/%Y'),'Samara','Jefferson')

