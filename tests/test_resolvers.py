from unittest import IsolatedAsyncioTestCase
from graphql import graphql
from ariadne import make_executable_schema, load_schema_from_path
import sys
sys.path.append('.')
from GraphQLAPI.resolvers import resolvers

class test_resolvers(IsolatedAsyncioTestCase):
    def setUp(self):
        self.schema = make_executable_schema(
            load_schema_from_path('./GraphQLAPI/Schemas/'), 
            resolvers)
    
    async def test_hello(self):
        result = await graphql(self.schema, "{hello}")
        self.assertEqual(result.data['hello'], "Hello!")
    
    async def test_helloThere(self):
        result = await graphql(self.schema, "{helloThere}")
        self.assertEqual(result.data['helloThere'], "Hello There!")