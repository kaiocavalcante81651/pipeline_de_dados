import clickhouse_connect

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
        ORDER BY id
""")