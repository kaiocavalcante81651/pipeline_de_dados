from ingestion.ingestion import minio
import clickhouse_connect

try:
    # Cria o cliente
    client = clickhouse_connect.get_client(
        host='localhost',       # Host onde o clickhouse está rodando
        port=8123,              # Porta HTTP
        username='default',     # Usuário padrão
        password='default',            # Senha, vazia por padrão
        database='default',     # Banco de dados padrão (para testar)
        secure=False            # Não utiliza HTTPS
    )
except TypeError as error:
    print(error)

result = client.query('SHOW TABLES')

# Executa as funções
if __name__ == '__main__':
    minio()
    print(result)

