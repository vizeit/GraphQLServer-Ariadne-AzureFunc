# GraphQL Server - Azure Function
Boilerplate [Serverless](https://en.wikipedia.org/wiki/Serverless_computing) implementation of [GraphQL](https://graphql.org/) server in [Python](https://www.python.org/) using [Ariadne](https://ariadnegraphql.org/)

## Features
- Implemented in Python
- Serverless
- Hosting on Azure Cloud
- Modular
- Support for WSGI and ASGI
- Lightweight

## Quickstart
### Pre-requisites
- Active [Azure cloud](https://azure.microsoft.com/en-us/) account
- Local development environment setup for [Azure functions using Python](https://docs.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=azure-cli%2Cbash%2Cbrowser)

### Steps
1. Clone the repo,
```
git clone https://github.com/vizeit/GraphQLServer-AzureFunc.git
``` 

2. Go to [*\_\_init\_\_.py*](/GraphQLAPI/__init__.py)

3. Import *GraphQL* class from either *WSGI* or *ASGI* module of *Ariadne* 
```
from ariadne.wsgi import GraphQL
```
*or*
```
from ariadne.asgi import GraphQL
```
4. Import *WsgiMiddleware* or *AsgiMiddleware* class from *azure.functions* module
```
from azure.functions import WsgiMiddleware
```
*or*
```
from azure.functions import AsgiMiddleware
```

5. Return *WsgiMiddleware* or *AsgiMiddleware* object from the *main* function w.r.t. your import in 3 and 4 above
```
return WsgiMiddleware(app).handle(req, context)
```
*or*
```
return AsgiMiddleware(app).handle(req, context)
```

6. Define GraphQL schema under [*Schemas*](/GraphQLAPI/Schemas/schema.graphql) folder

7. Write GraphQL resolvers for the schema in [*resolvers.py*](/GraphQLAPI/resolvers.py)