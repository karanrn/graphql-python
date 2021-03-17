from flask import Flask
from flask_graphql import GraphQLView
import graphene

from database import engine, db_session
import users.models
import books.models
from schema import schema

# Bind engine to models
users.models.Base.metadata.create_all(bind=engine)
books.models.Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.debug = True

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
    return 'Welcome!'

if __name__ == '__main__':
    app.run()