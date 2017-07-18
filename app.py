from flask import Flask, request, jsonify
from config.dev import DevConfig
import json
from models.Shared import db
from models.User import User

app = Flask(__name__)

@app.route('/user', methods=['POST' , 'GET'])
def create_user():
    if request.method == 'POST':
        data = request.json
        username = data.get("username")
        email = data.get("email")
        user = User(username, email)

        try:
            user.save()
            response = user._toJson_()
            response.status_code = 201
            return response
        except Exception as e:
            response = jsonify({
                    'error': e.message,
            })
            response.status_code = 400
            return response

@app.route('/user/<username>')
def getUser(username):
    try:
        data = request.json
        user = User.query.filter_by(username=username).first()
        response = user._toJson_()
        response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({
                    'error': e.message,
        })
        response.status_code = 400
        return response


if __name__ == '__main__':
    app.config.from_object(DevConfig)
    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='0.0.0.0')