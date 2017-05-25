from webapp import app, views, config


def main():
    host = config.get_variable('HOST', 'localhost')
    port = int(config.get_variable('PORT', '5000'))
    app.run(host=host, port=port, debug=True)
