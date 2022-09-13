from flask import Blueprint, jsonify, request
import uuid

# Models
from models.modeloGrupos import modeloGrupos

main = Blueprint('grupos_blueprint', __name__)


@main.route('/')
def get_grupos():
    try:
        grupos = modeloGrupos.get_grupos()
        return jsonify(grupos)
    except Exception as ex:
        return jsonify({'message':  str(ex)}), 500