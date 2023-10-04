from model import *

class CategoriaDao:

    @classmethod
    def cadastrar_categoria(cls, categoria:Categoria):
        with open('categorias.txt','a') as cat:
            cat.writelines(f'{categoria.nome} - {categoria.descricao}\n')

    @classmethod
    def recuperar(cls):
        with open('categorias.txt','r') as cat:
            categorias = cat.readlines()
            categorias.sort()

    @classmethod
    def atualizar(cls):
        with open('categorias.txt','w') as cat:
            for c in categorias:
                cat.writelines(c)