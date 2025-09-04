# pipeline_de_dados

Descrição

O projeto foi criado utilizando o conceito de contêineres com Docker. Com o docker,
foram criados dois servidores, um utilizando a imagem do Minio ( Object Storage ), utilizado
para armazenamento de objetos; o outro servidor foi criado com a imagem do Clickhouse, um
banco de dados para data warehouse robusto e escalável para a criação de tabelas. Além
disso, foram criados scripts python para fazer toda a manipulação dos dados.
A estrutura do projeto foi criada para se conectar ao Minio e acessar os dados do
arquivo .CSV que esta armazenado no bucket, feito isso, esses dados são inseridos no banco
de dados Clickhouse e em seguida são acessados, manipulados, tratados e exibidos em um
dashboard criado com Streamlit.

Configuração do Ambiente

O ambiente foi criado utilizando o poetry, uma ferramenta de gerenciamento de
dependências e empacotamento para projetos Python.
O poetry gera o arquivo pyproject.toml onde gerenciamos e guardamos todas as
dependências necessárias.
Instalamos bibliotecas python, como pandas para dataframes, streamlit para criação
do dashboard e plotly para a criação dos gráficos.
Definimos o arquivo Dockerfile que carrega uma imagem python personalizada para
executar o arquivo principal e o docker-compose.yml que gerencia todos os serviços
necessários em conjunto.
Na pasta ingestion, foi criado o arquivo objeto.py, que ficou responsável por se
conectar ao Minio e retornar o objeto como um dataframe.
Na pasta database, foi criado o arquivo db.py, que recebe o dataframe com os
dados do objeto, se conecta ao banco de dados Clickhouse, cria um banco de dados, cria
uma tabela e insere os dados do dataframe na tabela criada. Feito isso, ele também cria as
funções necessárias para chamar as views que foram criadas no banco de dados.
A pasta dashboard, guarda o arquivo apresentacao.py, que recebe os dados
retornados pelas views e cria o dashboard com streamlit para apresentar os dados tanto em
tabelas quanto em gráficos.
O arquivo app.py é o ponto de entrada da aplicação e executas todas as funções.
Para iniciar o fluxo basta digitar "docker compose up –-build" para colocar os contêineres
em execução, a porta 5000 exibirá o dashboard com streamlit onde o usuário poderá
escolher no menu lateral a exibição das tabelas ou gráficos.

<img width="1576" height="886" alt="exibindo_tabelas" src="https://github.com/user-attachments/assets/5c1469fa-e916-4dd7-842c-75666b6d69f6" />



<img width="1576" height="886" alt="exibindo_graficos" src="https://github.com/user-attachments/assets/2ee0676d-8261-4ca7-b07c-7927d243897c" />
