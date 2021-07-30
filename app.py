from flask import Flask, request
from flask_restful import Resource, Api
from security import authenticate, identity
from flask_jwt import JWT, jwt_required
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# in order to know when an object had changed but not being saved to the database, the extension sqlalchemy was
# tracking every change that we made to sql alchemy session and it took some resources,
# now we are turning it off coz sqlalchemy main library has own modification tracker
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'vaibhav'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


db.init_app(app)

# jwt below creates a endpoint ('/auth')
# when we call /auth, we send it username and password, jwt sends that to authenticate password, we get correct
# user object from return that. That becomes identity. then auth endpoint returns jwt token
# we can send that JWT token with the next request we make. then jwt calls identity function to see jwt is valid and
# identify the user
jwt = JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run()
