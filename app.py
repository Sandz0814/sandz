import os

from flask import Flask, render_template, jsonify, request, make_response
from functools import wraps
import datetime
import jwt

app = Flask(__name__)


app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 403

        return f(*args, **kwargs)
    return decorated


@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        token = jwt.encode(
            {'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
            app.config['SECRET_KEY'],
            algorithm="HS256"
        )
        return jsonify({'token': token if isinstance(token, str) else token.decode('UTF-8')})

    return make_response('Invalid credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/')
@token_required
def home():
    # Example Python data
    message = "Hello, welcome to my website"
    items = ["Item 1", "Item 2", "Item 3"]
    name = {
        "email": "sandrojimena0814@gmail.com",
        "password": 'GAB7YT7Y3U',
        "username": 'andy09'
    }

    # Render the HTML templates and pass Python data to it
    return render_template('index.html', message=message, items=items, name=name)


if __name__ == '__main__':
    app.run(debug=True, port=5002)

