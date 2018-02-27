from flask import Flask
from flask_restful import Resource, Api
from credenciais import make_query_discovery
from logistica_discovery import get_json_empresas
from logistica_discovery import get_x

app = Flask(__name__)
api = Api(app)

class DiscoveryQuery(Resource):
    def get(self,query):
        retrn = make_query_discovery(query)
        # retrn = get_x()
        json_empresas = get_json_empresas(retrn)
        return json_empresas

class NLUQuerry(Resource):
    def get(self,query):
        pass

class Index(Resource):
    def get(self):
        return "home"

api.add_resource(DiscoveryQuery, '/discovery/<string:query>')
api.add_resource(NLUQuerry, '//<string:query>')

api.add_resource(Index, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')