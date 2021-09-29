# CNAB - Movimentações Financeiras

O CNAB - Movimentações Financeiras foi construido usando `Python`(`Django` + `Django Rest FrameWork`) no seu Backend, `HTML`, `CSS` e `JS` no seu Frontend e `PostgreSQL` no banco de dados.  

Este projeto é um website com o intuito de parsear e importar dados de transações advindos do CNAB. A importação deve ser feita de maneira padronizada por meio de um arquivo .txt com a transações organizadas em linhas. 

Após importação feita, este projeto também conta com uma view de listagem, mostrando todas as importações, seus dados e alguns dados adicionais como: saldo daquele cpf e total gasto e total até o momento daquela transação, natureza e etc... 

Além do mais, o CNAB Movimentações também disponibliza o acesso a todas a movimentações por meio de uma API. 

## API

Para fazer uso dessa api, basta ter acesso a esses dados basta enviar uma requisição do tipo `GET` para `api/v1/movimentacao` e terá a seguinte response:
```json
GET /api/v1/movimentacao

# A api responderá com uma lista de transações tal qual o exemplo abaixo
[
    {
        "id": 211,
        "tipo": "Financiamento",
        "natureza": "saida",
        "saldo": -142.0,
        "data": "2019-03-01T15:34:53",
        "valor": "142.00",
        "cpf": "09620676017",
        "cartao": "4753****3153",
        "dono_loja": "JOÃO MACEDO",
        "nome_loja": "BAR DO JOÃO"
    },
]
```

## Preparando ambiente de homologação

Inicialmente instale o [docker](https://docs.docker.com/engine/install/ubuntu/) e o [docker-compose](https://docs.docker.com/compose/install/), clone o projeto e abra um terminal dentro da pasta. Neste terminal rode os seguintes comandos:
```bash
./docker-build.sh
```
Ao fim desse processo, o servidor estará rodando na url: `http://localhost:8080`.

## Preparando ambiente de desenvolvimento

Inicialmente clone o projeto e abra um terminal dentro da pasta. Neste terminal rode os seguintes comandos:

```bash
# Instalando lib para isolar os modulos python que será 
# usado no projeto dos demais modulos
python3 -m pip install virtualenv
python3 -m virtualenv .venv
activate ./.venv/bin/activate

# Com a virtualenv ativada, não é necessário especificar 
# a versão do python com 'python3 -m'
# Instalando modulos que será usados pelo projeto
pip install -r requirements.txt
```

Ao fim desses comandos, é necessário configurar o banco de dados para o desejados. Segue um passo a passo de como fazer essa configuração:
```bash
psql -U {username} -c "CREATE DATABASE {nome_do_banco}"
```
Após essa linha, será necessário a digitação da senha do postgres. Se sua senha estiver correta, seu banco será criado. O próximo passo, é configurar a conexão do seu banco com o django. Para tal, abra o arquivo `.env.dev` que está na raiz da pasta `/app` com o seguinte comando:
```bash
# Abrir com o Nano
nano app/.env.dev

# Abrir com o vim
vim app/.env.dev
```
Este arquivo é onde se localizam as variáveis que são responsáveis pela conexão com o banco de dados, mude-as de acordo com as suas credenciais. Segue um exemplo:
```bash
DB_NAME=movimentacoes # nome do banco
DB_USER=postgres # user do postgres
DB_PASSWD=postgres # password do postgres
DB_HOST=localhost # host do postgres
DB_PORT=5432 # porta do postgres
```
Por fim, migre as tabelas do django para o seu postgres e rode a aplicação:
```bash
# migrar as alterações e adições do 
# django para o postgres
python manage.py migrate 

# rodar o projeto na url: http://localhost:8000
python manage.py runserver
```