# Movile Next 3 Backend - Delivery Programado

Esse projeto consiste no trabalho de conclusão de curso do 3º Movile Next ministrado em fevereiro de 2019.  

## O Problema

O problema consiste realizar um pedido programado em uma plataforma de delivery de comida, como o iFood.

O cliente escolhe o dia e horário que gostaria de receber o pedido. Escolhe um dos restautantes disponíveis. Seleciona os itens que gostaria de perdir. Faz login na sua conta e finaliza o pedido.

Esse pedido deve ser entregue no dia e na hora que o cliente selecionou.


## A Solução

A solução proposta consiste em criar um middleware entre o cliente e a plataforma de delivery de comida (provider). 

O cliente se conecta ao middleware via RestAPI e o middleware faz a conexão com o provider.

O pedido fica represado no middleware até o dia e horário que o cliente selecionou para entrega. Quando essa data chegar o pedido é enviado ao provider como um delivery comum.


#### Arquitetura

A solução possui dois projetos. São eles:

- **ScheduledDeliveryWebApplication**
- **IfoodMockAPI**

Os projetos foram implementados utilizando o web framework [Flask](http://flask.pocoo.org/) com [Python 3.6](https://docs.python.org/3.6/).

A base de dados escolhida para persistência dos dados foi o [Postgres](https://www.postgresql.org/).

Todos os projetos são executados em containers [Docker](https://docs.docker.com/), tanto as aplicações quanto o banco de dados. Os containers são orquestrados via [Docker Compose](https://docs.docker.com/compose/overview/).

Cada projeto possui um arquivo *Dockerfile* com as configurações do ambiente em que a aplicação é executada. 

Na raiz do projeto, o arquivo *docker-compose.yml*, possui as configurações de todos os serviços necessários pra a solução ser executada. 

O solução possui um projeto core, **ScheduledDeliveryWebApplication**, responsável pelas APIs de conexão com o cliente e o as interfaces de conexão com o provider.


##### ScheduledDeliveryWebApplication

Essa aplicação é o core da solução, o middleware propriamente dito. Ela é dividida em 4 módulos, são eles:

- **models**: Possui a modelagem dos dados da aplicação e suas invariantes. 
- **providers**: Responsável pela interface com o provider, contentos os métodos necessários para pegar ou salvar os dados da aplicação do provider.
- **resources**: Implementação das APIs Rest
- **validator**: Classes de validação de formato de dados


##### IfoodMockAPI

Aplicação criada para simular as respostas das APIs do IFood. Possui 4 APIs Rest que retornam as informações no formato de JSON.

- Catalog: Retorna os restaurantes disponíveis por endereço
- Merchant: Retorna o cardádio de um restaurante específico
- Login: Simula a autenticação de um cliente e retorna seus dados
- Order: Simula a criação de uma order e retorna o status "CREATED"


#### Exemplo de uso

- API de catálogo

```
curl -X POST \
  http://0.0.0.0:8000/catalog \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
  "country": "Belgium",
  "state": "Alaska",
  "city": "Bentley",
  "neighborhood": "ut",
  "streetName": "Wilson Street",
  "streetNumber": 934,
  "postalCode": 70914730,
  "complement": "",
  "latitude": 64.653927,
  "longitude": 94.998853,
  "deliveryDateTime": "2019-03-20T19:00:00 +03:00"
}'
```

- API de menu por restautante

```
curl -X GET \
  http://0.0.0.0:8000/merchant/10 \
  -H 'cache-control: no-cache'
```

- API de login

```
curl -X POST \
  http://0.0.0.0:8000/auth/login \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"username": "incididunt",
	"password": "excepteur"
}'
```

- API de agendamento de pedido

```
curl -X POST \
  http://0.0.0.0:8000/order \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"customerId": 1,
	"merchantId": 10,
	"deliveryAddress": {
        "country": "Saudi Arabia",
        "state": "Virgin Islands",
        "city": "Ribera",
        "neighborhood": "eu",
        "streetName": "Hopkins Street",
        "streetNumber": 887,
        "postalCode": 88634912,
        "complement": "",
        "latitude": 54.954462,
        "longitude": 120.48691
    },
    "deliveryDateTime": "2019-03-20T19:00:00.029810",
    "items": [
    	{
	      "name": "sunt",
	      "price": 5089,
	      "discount": 528,
	      "quantity": 35,
	      "addition": "",
	      "observations": ""
    	}
	]
}'
```

- API para criar o pedido

```
curl -X POST \
  http://0.0.0.0:8000/order/5 \
  -H 'cache-control: no-cache'
```


### Instruções de Execução

Para executar o projeto basta baixar o repositório e rodar o seguinte comando:

```
docker-compose up --build
```

## ToDo

- Implemtação dos testes automatizados
- Criação da task de envio de pedidos
