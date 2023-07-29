from webapp import app
from webapp import bcrypt
from webapp.models.users import Users
from flask import request
from webapp import db
from flask import jsonify, request
from flask_bcrypt import Bcrypt

@app.route('/users', methods=['get'])
def getUsers():
    users = []
    fetched_users = Users.query.all()
    for user in fetched_users:
        user_object = {}
        user_object["id"] = i.id
        user_object["name"] = i.email
        users.append(user_object)
    return jsonify(users) 


@app.route('/user/add', methods=['POST'])
def addUser():
    data = request.get_json()
    final_name = data['name']
    users = Users.query.all()
    user = Users.query.filter(Users.name == final_name).first()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    if user == None:
        newUser = Users( name = data['name'], password = hashed_password, phone_number =  data['phone_number'], email =  data['email'], dob = data['dob'])
        db.session.add(newUser)
        db.session.commit()
        done = "sucess added"
        print(done)
        return jsonify(done), 200 
    else:
        print("inside else")
        err = "The Username is ALready Taken, Please try other username"
        print(err)
        return jsonify(err), 422  
    return jsonify(done), 200


@app.route('/user/delete', methods=['get'])
def deleteUser():
    data = request.args
    id = data['id']
    print(id)
    Users.query.filter_by(id=id).delete()
    db.session.commit()
    
    return "sucess delete"


@app.route('/user/update', methods=["POST"])
def edit_user_profile():
    data = request.get_json()
    print(f"data: {data}")
    name = data['name']
    phone_number =  data['phone_number']
    email =  data['email']
    dob = data['dob']

    user = Users.query.filter(Users.id == data['id']).first()

    user.name = name
    user.phone_number = phone_number
    user.email = email
    user.dob = dob
    db.session.add(user)
    db.session.commit()
    return "sucess updated"


@app.route('/login/validation', methods=["POST"])
def login_validation():
    data = request.get_json()
    gmail = data['gmail']
    password = data['password']
    print(gmail)
    print(password)
    users = Users.query.all()
    err = ''
    for i in users:
        print(f"checking {gmail} : {i.gmail}")
        if gmail == i.gmail: 
            print("gmail is correct")
            if password == i.password:
                is_valid = bcrypt.check_password_hash(i.password, password)
                print(is_valid)

                return jsonify("response")
            else:
                err = "password"
                print(err)
                return jsonify(err), 422
    else:
        err = "Username"
        print(err)
        return jsonify(err), 422

    return jsonify("access_token"), 200 


