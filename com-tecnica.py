class Pedido:
    def __init__(self, quantidade, preco_item):
        self.quantidade = quantidade
        self.preco_item = preco_item

    def preco_base(self):
        return self.quantidade * self.preco_item

    def preco_final(self):
        if self.preco_base() > 1000:
            return self.preco_base() * 0.95
        return self.preco_base() * 0.98

    def resumo(self):
        return f'Total bruto: {self.preco_base()}'
