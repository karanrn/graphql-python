from flask import Flask
from flask_graphql import GraphQLView
import graphene

from app_relay.database import engine, db_session
import app_relay.users.models
import app_relay.books.models
from app_relay.schema import schema

def create_app():
    # Bind engine to models
    app_relay.users.models.Base.metadata.create_all(bind=engine)
    app_relay.books.models.Base.metadata.create_all(bind=engine)

    appl = Flask(__name__)
    appl.debug = True

    # Routes
    appl.add_url_rule(
        '/graphql-api',
        view_func=GraphQLView.as_view(
            'graphql',
            schema = schema,
            graphiql=True
        )
    )

    @appl.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @appl.route('/')
    def index():
        return 'Welcome!'
    
    return appl