class Clientes:
    def __init__(self):
        self.clientes = {}

    def create_client(self, nome, telefone, idade, renda, peso):
        cliente = {
            'nome': nome,
            'telefone': telefone,
            'idade': idade,
            'renda': renda,
            'peso': peso
        }
        self.clientes[nome] = cliente
        print('Cliente', nome, 'adicionado com sucesso!')

    def update_name(self, nome_antigo, nome_novo):
        if nome_antigo in self.clientes.keys():
            cliente = self.clientes[nome_antigo]
            cliente['nome'] = nome_novo
            self.clientes[nome_novo] = cliente
            del self.clientes[nome_antigo]
            print('Nome atualizado com sucesso:', nome_antigo, '->', nome_novo)
        else:
            print('Cliente não encontrado.')

    def update_phone(self, nome, novo_telefone):
        if nome in self.clientes.keys():
            cliente = self.clientes[nome]
            cliente['telefone'] = novo_telefone
            print('Telefone de', nome, 'atualizado com sucesso!')
        else:
            print('Cliente não encontrado.')


# Exemplo de uso
conjunto_clientes = Clientes()

# Criar clientes
conjunto_clientes.create_client('João', '123456789', 30, 5000.00, 70.5)
conjunto_clientes.create_client('Maria', '987654321', 25, 4000.00, 60.2)
conjunto_clientes.create_client('Pedro', '555555555', 40, 6000.00, 80.0)

# Atualizar nome de um cliente
conjunto_clientes.update_name('João', 'João Silva')

# Atualizar telefone de um cliente
conjunto_clientes.update_phone('Maria', '999999999')    
