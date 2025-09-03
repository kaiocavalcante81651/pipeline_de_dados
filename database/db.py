import clickhouse_connect
from ingestion.objeto import minio_objeto
import pandas as pd

objeto = minio_objeto()

try:
    # Cria o cliente
    client = clickhouse_connect.get_client(
        host='localhost',       # Host onde o clickhouse está rodando
        port=8123,              # Porta HTTP
        username='default',     # Usuário padrão
        password='default',            # Senha, vazia por padrão
        database='',     # Banco de dados padrão (para testar)
        secure=False            # Não utiliza HTTPS
    )
except TypeError as error:
    print(error)

def criar_banco_de_dados():
    client.command("CREATE DATABASE IF NOT EXISTS db_iot_data")
    client.command("USE db_iot_data")
    client.command("""
        CREATE TABLE IF NOT EXISTS dados_iot (
            id UUID DEFAULT generateUUIDv4(),
            logs String,
            sala String,
            data DateTime,
            temperatura Int32,
            "out/in" String
        )
        ENGINE = MergeTree()
        PRIMARY KEY id
        ORDER BY id
    """)
    
def inserir_dados():
    df = objeto.rename(columns={
        'id'        : 'logs',
        'room_id/id': 'sala',
        'noted_date': 'data',
        'temp'      : 'temperatura',
        'out/in'    : 'out/in'
    })
    client.insert_df(table='dados_iot', df=df)

def retorna_dados():
    dados = client.query_df("SELECT * FROM dados_iot")
    return dados

def temperaturas():

    consulta = "SELECT * FROM temp_por_dispositivo;"

    result = client.query(consulta)
    df = pd.DataFrame(result.result_rows, columns=result.column_names)
    return df

def data_temperatura():

    consulta = "SELECT * FROM temp_por_data;"

    result = client.query(consulta)
    df = pd.DataFrame(result.result_rows, columns=result.column_names)
    return df