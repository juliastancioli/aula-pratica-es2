import unittest
from utils import Clientes

class TestClientes(unittest.TestCase):
    def setUp(self):
        self.conjunto_clientes = Clientes()
        self.conjunto_clientes.create_client('João', '123456789', 30, 5000.00, 70.5)
        self.conjunto_clientes.create_client('Maria', '987654321', 25, 4000.00, 60.2)

    def test_create_client(self):
        self.assertEqual(len(self.conjunto_clientes.clientes), 2)
        self.conjunto_clientes.create_client('Pedro', '555555555', 40, 6000.00, 80.0)
        self.assertEqual(len(self.conjunto_clientes.clientes), 3)
        self.assertIn('Pedro', self.conjunto_clientes.clientes)

    def test_update_name(self):
        self.conjunto_clientes.update_name('João', 'João Silva')
        self.assertIn('João Silva', self.conjunto_clientes.clientes)
        self.assertNotIn('João', self.conjunto_clientes.clientes)

    def test_update_phone(self):
        self.conjunto_clientes.update_phone('Maria', '999999999')
        self.assertEqual(self.conjunto_clientes.clientes['Maria']['telefone'], '999999999')

    def test_update_name_nonexistent_client(self):
        self.conjunto_clientes.update_name('Pedro', 'Pedro Silva')
        self.assertNotIn('Pedro Silva', self.conjunto_clientes.clientes)
        self.assertNotIn('Pedro', self.conjunto_clientes.clientes)

    def test_update_phone_nonexistent_client(self):
        self.conjunto_clientes.update_phone('Carlos', '888888888')
        self.assertNotIn('Carlos', self.conjunto_clientes.clientes)

if __name__ == '__main__':
    unittest.main()
