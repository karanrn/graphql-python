from flask import Flask, _app_ctx_stack, jsonify
from flask_cors import CORS
from flask_graphql import GraphQLView
import graphene
from sqlalchemy.orm import scoped_session
import json

from database import SessionLocal, engine
import users.models
import books.models

users.models.Base.metadata.create_all(bind=engine)
books.models.Base.metadata.create_all(bind=engine)
# import users.schema
# import books.schema

# class Query(
#     users.schema.Query,
#     books.schema.Query,
#     graphene.ObjectType
# ):
#     pass

# schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.debug = True
CORS(app)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)
# Configs
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

# # Modules
# db = SQLAlchemy(app)

# Routes
# app.add_url_rule(
#     '/graphql-api',
#     view_func=GraphQLView.as_view(
#         'graphql',
#         schema = None,
#         graphiql=True
#     )
# )

@app.route('/')
def index():
    records = app.session.query(users.models.User).all()
    # return 'Welcome!'
    print(records[0])
    return jsonify([record.to_dict() for record in records])

if __name__ == '__main__':
    app.run()