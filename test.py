import unittest
import grpc
import seu_servico_pb2
import seu_servico_pb2_grpc
from server import SeuServico
from client import inserir_dado

class SeuServicoTest(unittest.TestCase):

    def test_inserir_dado(self):
        # Configuração inicial do servidor gRPC
        self.server = grpc.server(grpc.InsecureServer())
        self.seu_servico = SeuServico()
        seu_servico_pb2_grpc.add_SeuServicoServicer_to_server(self.seu_servico, self.server)
        self.server.add_insecure_port('[::]:50051')
        self.server.start()

        # Configuração inicial do cliente gRPC
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = seu_servico_pb2_grpc.SeuServicoStub(channel)
        
        # Executa o teste de inserção de dado
        chave = 1
        desc = "Descrição do dado"
        valor = 3.14

        status = inserir_dado(self.stub, chave, desc, valor)

        # Verifica se o status de retorno é 0 (inserção bem-sucedida)
        self.assertEqual(status, 0)
        
        # Executa o teste de inserção de dado
        chave = 1
        desc = "Descrição do dado"
        valor = 18

        status = inserir_dado(self.stub, chave, desc, valor)

        # Verifica se o status de retorno é 1 (troca do valor)
        self.assertEqual(status, 1)
        
        # Encerramento do servidor gRPC
        self.server.stop(0)

if __name__ == '__main__':
    unittest.main()
