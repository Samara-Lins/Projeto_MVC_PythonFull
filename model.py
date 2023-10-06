import datetime

class Categoria:

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Produto:

    def __init__(self, nome:str, categoria:Categoria, preco:float, estoque:int):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.estoque = estoque

class Pessoa:

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Fornecedor(Pessoa):

    def __init__(self, id:str, nome:str, cpf:str, produtos_fornecidos:list, telefone:str):
        super().__init__(nome, cpf)
        self.produtos_fornecidos = produtos_fornecidos
        self.telefone = telefone
        self.id = id

class Cliente(Pessoa):

    def __init__(self, id:str, nome:str, cpf:str, email:str):
        super().__init__(nome, cpf)
        self.id = id
        self.email = email

class Funcionario(Pessoa):

    def __init__(self, nome, cpf, cargo, salario):
        super().__init__(nome, cpf)
        self.cargo = cargo
        self.salario = salario

class Venda:

    def __init__(self, itensVendidos:dict, data, vendedor:Funcionario, comprador:Cliente):
        self.itensVendidos = itensVendidos
        self.data = data
        self.vendedor = vendedor
        self.comprador = comprador
