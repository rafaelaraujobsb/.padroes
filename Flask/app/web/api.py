#!/usr/bin/python3.6

from flask import Blueprint


api = Blueprint('api', __name__)


@api.route('/')
def index():
    return 'OK'