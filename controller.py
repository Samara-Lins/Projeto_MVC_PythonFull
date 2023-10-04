from dao import *
from model import categorias,Categoria

class CategoriaController:

    @classmethod
    def editar_categoria_nome(cls, nome, novo_nome):
        CategoriaDao.recuperar()
        for c in categorias:
            if c[0:len(nome)] == nome:
                c.replace(c[0:len(nome)],novo_nome)
        print(categorias)
        CategoriaDao.atualizar()

try:
    CategoriaDao.recuperar()

except FileNotFoundError:
    pass

c1 = Categoria('Hortifruti','Frutas legumes e verduras, produtos da horta e do pomar')

CategoriaDao.recuperar()
print(categorias)


