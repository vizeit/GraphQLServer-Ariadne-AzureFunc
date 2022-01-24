import azure.functions as func
from azure.functions import AsgiMiddleware

from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from GraphQLAPI.resolvers import resolvers

schema = make_executable_schema(
    load_schema_from_path('./GraphQLAPI/Schemas/'), 
    resolvers)
app = GraphQL(schema, debug=True)

def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return AsgiMiddleware(app).handle(req, context)
