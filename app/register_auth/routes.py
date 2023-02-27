from forms import UserLoginForm
from helpers import token_required
from models import User, Register, db, check_password_hash, user_schema, users_schema, register_schema, registers_schema
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify

from flask_login import login_user, logout_user, LoginManager, current_user, login_required 


auth2 = Blueprint('auth2', __name__, url_prefix = '/auth2')

@auth2.route('/getdata')
def getdata():
    return {'yee': 'haw'}



@auth2.route('/register', methods = ['POST']) 
def user_register():
    email = request.json['email']
    first_name = request.json['first_name'] 
    last_name = request.json['last_name']
    password = request.json['password']
    # user_token = current_user_token.token

    print(f'BIG TESTER: ')

    register = Register(first_name, last_name, email, password) 

    db.session.add(register) 
    db.session.commit() 

    response = register_schema.dump(register)
    return jsonify(response)


@auth2.route('/register', methods = ['GET'])
def get_users(): # current_user_token inside parenthesis for authentication
    # a_user = current_user_token.token
    all_users = Register.query.all()
    response = registers_schema.dump(all_users)
    return jsonify(response)    
  
@auth2.route('/register/<id>', methods = ['GET'])
def get_single_user(id):
    # a_user = current_user_token.token
    single_user = Register.query.get(id)
    response = register_schema.dump(single_user)
    return jsonify(response)



@auth2.route('/user_logout')
def logout():
    logout_user() 
    return redirect(url_for('site.home'))

