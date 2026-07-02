class Transacao_model:

    def __init__(
        self,
        valor,
        descricao,
        categoria,
        forma_pagamento,
        data,
        tipo
    ):
        self.valor = valor
        self.descricao = descricao
        self.categoria = categoria
        self.forma_pagamento = forma_pagamento
        self.data = data
        self.tipo = tipo