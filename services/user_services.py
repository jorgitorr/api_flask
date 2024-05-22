from flask import Blueprint
from flask import request
from db import db  
from config.mongo import mongo

my_users = Blueprint("my_users",__name__)

@my_users.route('/', methods=['GET'])
def get_all_users():
    return "Obtener todos los usuarios"

@my_users.route('/<id>',methods=['GET'])
def get_one_user(id):
    return "Obtenemos un usuario"

@my_users.route('/',methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email',None)
    name = data.get('name',None)
    password = data.get('password',None)
    auth = data.get('auth',False)

    if email and len(password) > 6:
        response = mongo.db.my_users.insert_one({
            'email':email, 
            'name':name, 
            'password':password, 
            'auth':auth})

        result = {
            'id':str(response.inserted_id),'email':email, 'name':name, 'password':password, 'auth':auth, 'message':'Usuario creado correctamente'
        }
        return result
    else:
        return 'Invalid payload',400

@my_users.route('/<id>',methods=['PUT'])
def update_user(id):
    return "Actualizamos el usuario"

@my_users.route('/<id>',methods=['DELETE'])
def delete_user(id):
    return "Borramos el usuario"
