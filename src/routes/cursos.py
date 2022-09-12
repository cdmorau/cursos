from flask import Blueprint, jsonify, request
import uuid

# Models
from models.modeloCursos import modeloCursos

main = Blueprint('cursos_blueprint', __name__)


@main.route('/')
def get_cursos():
    try:
        cursos = modeloCursos.get_cursos()
        return jsonify(cursos)
    except Exception as ex:
        return jsonify({'message':  str(ex)}), 500

@main.route('/<id>')
def get_curso(id):
    try:
        curso = modeloCursos.get_curso(id)
        if curso != None:
            return jsonify(curso)
        else: 
            return jsonify({}), 404
    except Exception as ex:
        return jsonify({'message':  str(ex)}), 500