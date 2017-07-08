from flask import Flask, request
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
            db.session.add(user)
            db.session.commit()
            return json.dumps(user)
        except Exception as e:
            return json.dumps(e.message)


if __name__ == '__main__':
    app.config.from_object(DevConfig)
    db.init_app(app)
    db.app = app
    db.create_all()
    app.run(host='0.0.0.0')