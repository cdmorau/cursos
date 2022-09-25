from flask import Flask
from flask_cors import CORS

from config import config

# Routes
from routes import cursos
from routes import grupos

app = Flask(__name__)

CORS(app, resources={"*": {"origins": "http://localhost:5000"}})


def page_not_found(error):
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # Blueprints
    app.register_blueprint(cursos.main, url_prefix='/api/cursos')
    app.register_blueprint(grupos.main, url_prefix='/api/grupos')

    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run(host="0.0.0.0", port=5000, debug=True)