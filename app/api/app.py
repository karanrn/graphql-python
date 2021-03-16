from flask import Flask, _app_ctx_stack, jsonify
from flask_graphql import GraphQLView
import graphene
from sqlalchemy.orm import scoped_session

from database import SessionLocal, engine, db_session
import users.models
import books.models
from schema import schema, BookObject
# import users.schema
# import books.schema

# class Query(
#     users.schema.Query,
#     books.schema.Query,
#     graphene.ObjectType
# ):
#     pass

# schema = graphene.Schema(query=Query)

users.models.Base.metadata.create_all(bind=engine)
books.models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.debug = True

# Configs
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# # Modules
# db = SQLAlchemy(app)

# Routes
app.add_url_rule(
    '/graphql-api',
    view_func=GraphQLView.as_view(
        'graphql',
        schema = schema,
        graphiql=True
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    # records = app.session.query(users.models.User).all()
    return 'Welcome!'
    # return jsonify([record.to_dict() for record in records])

if __name__ == '__main__':
    app.run()