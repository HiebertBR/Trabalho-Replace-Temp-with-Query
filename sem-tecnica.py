class Pedido:
    def __init__(self, quantidade, preco_item):
        self.quantidade = quantidade
        self.preco_item = preco_item

    def preco_final(self):
        base = self.quantidade * self.preco_item
        if base > 1000:
            return base * 0.95
        return base * 0.98

    def resumo(self):
        base = self.quantidade * self.preco_item
        return f'Total bruto: {base}'