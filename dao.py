from model import *

class CategoriaDao:

    @classmethod
    def cadastrar_categoria(cls, categoria:Categoria):
        with open('categorias.txt','a') as cat:
            cat.writelines(f'{categoria.nome}|{categoria.descricao}\n')


    @classmethod
    def ler(cls):
        with open('categorias.txt','r') as cat:
            categorias = cat.readlines()
            remover_quebra = list(map(lambda x: x.replace('\n',''),categorias))
            lista_categorias = []
            for c in remover_quebra:
                l = c.split('|')
                lista_categorias.append(Categoria(l[0],l[1]))
            print(lista_categorias)

class VendaDao:

    @classmethod
    def efetuar_venda(cls,venda:Venda):
        with open('vendas.txt','a') as vend:
            for k,v in venda.itensVendidos:
                vend.writelines(f'{v} {k}')
            vend.writelines(f'{venda.vendedor}')
            vend.writelines(f'{venda.comprador}')
            vend.writelines(f'{venda.data}')

