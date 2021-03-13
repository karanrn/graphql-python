from flask import Flask
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from flask_graphql import GraphQLView
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy import SQLAlchemyConnectionField

app = Flask(__name__)
app.debug = True

# Configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# Modules
db = SQLAlchemy(app)

# Models
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    books = db.relationship('Book', backref='author')

    def __init__(self, username, email):
      self.username = username
      self.email = email

    def __repr__(self):
        return '' % self.id

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '' % self.title % self.description % self.year % self.author_id

# Schema Objects
class BookObject(SQLAlchemyObjectType):
    class Meta:
        model = Book
        interfaces = (graphene.relay.Node, )

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_books = SQLAlchemyConnectionField(BookObject)
    all_users = SQLAlchemyConnectionField(UserObject)

schema = graphene.Schema(query=Query)

# Routes
app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema = schema,
        graphiql=True
    )
)

@app.route('/')
def index():
    return 'Welcome!'

if __name__ == '__main__':
    app.run()