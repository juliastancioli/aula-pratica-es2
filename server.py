import grpc
from concurrent import futures
import seu_servico_pb2
import seu_servico_pb2_grpc

class SeuServico(seu_servico_pb2_grpc.SeuServicoServicer):
    def __init__(self):
        self.dicionario = {}

    def InserirDado(self, request, context):
        chave = request.chave
        desc = request.desc
        valor = request.valor

        if chave in self.dicionario:
            # Atualizar o conteúdo para a chave existente
            self.dicionario[chave]['desc'] = desc
            self.dicionario[chave]['valor'] = valor
            return seu_servico_pb2.Resultado(status=1)
        else:
            # Inserir uma nova entrada no dicionário
            self.dicionario[chave] = {'desc': desc, 'valor': valor}
            return seu_servico_pb2.Resultado(status=0)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
seu_servico_pb2_grpc.add_SeuServicoServicer_to_server(SeuServico(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
