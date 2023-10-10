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
            lista_vendas = []
            for li in VendaDao.vendas:
                sublista = []
                if li == '\n\n':
                    liindice = VendaDao.vendas.index(li)
                    sublista = [g for g in VendaDao.vendas if VendaDao.vendas.index(g) < liindice]
                    print(sublista[0])
                    indice = sublista.index('-----\n')
                    print(indice)
                    sublvd = sublista[0:indice]
                    sublista.remove('-----\n')
                    print(sublvd)
                    produtos = []
                    for s in sublvd:
                        d = s.split(' ')
                        dic = {d[0]:d[1]}
                        produtos.append(dic)
                    sublv = sublista[indice:]
                    lista_venda = [produtos]
                    for i in sublv:
                        lista_venda.append(i)
                    v = Venda(lista_venda[0],lista_venda[1],lista_venda[2],lista_venda[3])
                    lista_vendas.append(v)
                    for i in range(0,liindice+1):
                        VendaDao.vendas.remove(i)
                print(lista_vendas)