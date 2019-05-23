from flask import Flask
from flasgger import Swagger

from app.web.api import api_bp


template = {
    "swagger": "2.0",
    "info": {
        "title": "",
        "description": "",
        "version": ""
    },
    # "basePath": "/api",
    # "host": "localhost:5000",
    "consumes": [
        "application/json"
    ],
    "produces": [
        "application/json"
    ]
}

app = Flask(__name__)
Swagger(app, template=template)

app.register_blueprint(api_bp, url_prefix='/api')
