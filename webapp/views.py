import logging
from flask import render_template
from webapp import app

logger = logging.getLogger(__name__)


@app.route('/')
@app.route('/<string:name>')
def index(name=''):
    return render_template('index.html', name=name)
