from database.db import criar_banco_de_dados
from database.db import inserir_dados
from database.db import retorna_dados
from dashboard.apresentacao import exibir


# Executa as funções
if __name__ == '__main__':
    criar_banco_de_dados()
    #inserir_dados()
    exibir()