import connexion
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify


def post_greeting(name: str) -> str:
    return 'Hello {name}'.format(name=name)


def get_user(username: str) -> object:
    user = User.query.filter_by(username=username).first()

    # TODO: get first_or_none and do a 404 if none.

    return jsonify({
        'id': user.id,
        'username': user.username,
        'email': user.email
     })


# Boot up connexion app using the flask framework and add api:
cx = connexion.FlaskApp(__name__, port=9090, specification_dir='swagger/')
cx.add_api('api.yaml', swagger_ui=True, arguments={'title': 'Sample API'})

# Configure SQL Alchemy settings
# note on relative path: https://gist.github.com/ekiara/7676136
cx.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
cx.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(cx.app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


@cx.app.route('/')
def index():
    return 'Hello world!!!!!!!1'


#db.create_all()
#admin = User(username='admin', email='admin@example.com')
#db.session.add(admin)
#db.session.commit()


if __name__ == '__main__':
    cx.run()
