from webapp import app
from flask import render_template
from webapp import config


@app.route('/')
@app.route('/<string:name>')
def index(name=''):
    return render_template('index.html', name=name)


# remove later (use the run.py)
if __name__ == '__main__':
    host = config.get_variable('HOST', 'localhost')
    port = int(config.get_variable('PORT', '5000'))
    app.run(host=host, port=port, debug=True)
