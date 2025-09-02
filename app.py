from ingestion.ingestion import minio
from database.db import criar_banco_de_dados
import clickhouse_connect


df = minio()

try:
    # Cria o cliente
    client = clickhouse_connect.get_client(
        host='localhost',       # Host onde o clickhouse está rodando
        port=8123,              # Porta HTTP
        username='default',     # Usuário padrão
        password='default',            # Senha, vazia por padrão
        database='db_iot_data',     # Banco de dados padrão (para testar)
        secure=False            # Não utiliza HTTPS
    )
except TypeError as error:
    print(error)


def inserir_dados():
    new_df = df.rename(columns={
        'id': 'logs',
        'room_id/id': 'sala',
        'noted_date': 'data',
        'temp': 'temperatura',
        'out/in': 'out/in'
    })
    client.insert_df(table='dados_iot', df=new_df)

# Executa as funções
if __name__ == '__main__':
    criar_banco_de_dados()
    inserir_dados()
    

