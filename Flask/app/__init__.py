
from flask import Flask, render_template
from app.web.api import api


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


app.register_blueprint(api, url_prefix='/api')
