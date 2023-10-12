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
            for i in venda.itensVendidos:
                dic = i.items()
                for k, v in dic:
                    vend.writelines(f'{v} {k}\n')
            vend.writelines('-----\n')
            vend.writelines(f'{venda.vendedor}\n')
            vend.writelines(f'{venda.comprador}\n')
            vend.writelines(f'{venda.data}\n')
            vend.writelines('\n\n')

    @classmethod
    def ler(cls):
        with open('vendas.txt','r') as vend:
            VendaDao.vendas = vend.read()
            VendaDao.vendas = VendaDao.vendas.split('\n\n')
            for v in VendaDao.vendas:
                lista = v.split('-----\n')
                sub1 = lista[0]
                sub2 = lista[1]
                produtos = sub1.split('\n')
                print(produtos)
                sub2 = sub2.split('\n')
                print(sub2)