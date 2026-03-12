from flask import Flask
from flask_restful import Api
from flasgger import Swagger

from app.urls.routes import init_routes


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)


init_routes(api=api)