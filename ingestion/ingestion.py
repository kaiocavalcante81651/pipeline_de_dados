from minio import Minio
from minio.error import S3Error
import pandas as pd

# Conexão com o minio
try:
    client = Minio(
        "localhost:9000",           # Porta da API minio
        access_key="minioadmin",    # MINIO_ROOT_USER
        secret_key="minioadmin",    # MINIO_ROOT_PASSWORD
        secure=False                # protocolo HTTP
    )
except S3Error as error:
    print(error)


 # Variáveis com os nomes do bucket e do objeto
bucket_name = 'dados-iot'
object_name = 'IOT-temp.csv'

# Variável que recebe o objeto (arquivo csv) do minio
response = client.get_object(bucket_name, object_name)

def minio():
   # Carrega o arquivo com o pandas
    df = pd.read_csv(response)

    # Formata a coluna 'id'
    df["id"] = df['id'].str[16:]

    # Variáveis que armazenam quantidades de linhas e colunas
    num_linhas = df.shape[0]
    num_colunas = df.shape[1]
    
    return(
        # Exibe o arquivo, as 5 primeiras linhas
        print(df.head()),
        # Exibe dados sobre a estrutura do arquivo
        print(f'O arquivo contém: {num_linhas} linhas.'),
        print(f'O arquivo contém: {num_colunas} colunas.'),
        print('As colunas do arquivo são: ', df.columns.to_list())
    )