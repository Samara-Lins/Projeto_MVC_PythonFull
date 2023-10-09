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
            VendaDao.vendas = vend.readlines()
            vendas_separadas = VendaDao.vendas. 
            while '-----\n' in VendaDao.vendas:
                indice = VendaDao.vendas.index('-----\n')
                print(indice)
                sublvd = VendaDao.vendas[0:indice]
                VendaDao.vendas.remove('-----\n')
                print(sublvd)
                produtos = []
                for s in sublvd:
                    d = s.split(' ')
                    dic = {d[0]:d[1]}
                    produtos.append(dic)
                sublv = VendaDao.vendas[indice:]
                lista_venda = [produtos]
                for i in sublv:
                    lista_venda.append(i)
                v = Venda(lista_venda[0],lista_venda[1],lista_venda[2],lista_venda[3])
                lista_vendas = []
                lista_vendas.append(v)
            print(lista_vendas)