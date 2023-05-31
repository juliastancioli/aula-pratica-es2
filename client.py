import grpc
import seu_servico_pb2
import seu_servico_pb2_grpc


def inserir_dado(stub, chave, desc, valor):
    dado = seu_servico_pb2.Dado()
    dado.chave = chave
    dado.desc = desc
    dado.valor = valor

    resultado = stub.InserirDado(dado)
    return resultado.status

def main():
    # Código de inicialização do canal e stub gRPC
    channel = grpc.insecure_channel('localhost:50051')
    stub = seu_servico_pb2_grpc.SeuServicoStub(channel)
    # Código para conectar ao servidor gRPC

    # Loop para interagir com o usuário e chamar a função InserirDado
    while True:
        entrada = input("Digite o comando (I,ch,desc,val): ")
        comando, chave, desc, valor = entrada.split(",")

        if comando == "I":
            status = inserir_dado(stub, int(chave), desc, float(valor))
            print("Valor de retorno do procedimento:", status)
        else:
            print("Comando inválido. Tente novamente.")

    # Código para encerrar a conexão gRPC
    channel.close()

if __name__ == "__main__":
    main()
