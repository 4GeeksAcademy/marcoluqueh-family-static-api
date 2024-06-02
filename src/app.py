"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)


jackson_family = FamilyStructure("Jackson") # create the jackson family object


@app.errorhandler(APIException) # Handle/serialize errors like a JSON object
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code


@app.route('/') # generate sitemap with all your endpoints
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET', 'POST'])
def handle_hello():
    response_body = {}
    # this is how you can use the Family datastructure by calling its methods
    if request.method == 'GET':
        members = jackson_family.get_all_members()
        response_body["hello"] = "world"
        response_body["family"] = members
        return jsonify(response_body), 200
    if request.method == 'POST':
        data = request.json
        result = jackson_family.add_member(data)
        response_body["message"] = 'El endpoint funciona'
        response_body["results"] = data
        return response_body, 200


@app.route('/members/<int:id>', methods=['GET', 'DELETE', 'PUT'])
def handle_members(id):
    response_body = {}
    if request.method == 'GET':
        result = jackson_family.get_member(id)
        if result:
            print(result)
            response_body['message'] = 'Usuario encontrado'
            response_body['results'] = result
            return response_body, 200
        else:
            print(result)
            response_body['message'] = 'Usuario no existente'
            response_body['results'] = {}
            return response_body, 404
    if request.method == 'DELETE':
        result = jackson_family.delete_member(id)
        if result:
            print(result)
            response_body['message'] = 'Usuario eliminado'
            response_body['results'] = result
            return response_body, 200
        else:
            print(result)
            response_body['message'] = 'Usuario no existente'
            response_body['results'] = {}
            return response_body, 404



if __name__ == '__main__':
    # this only runs if `$ python src/app.py` is executed
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
