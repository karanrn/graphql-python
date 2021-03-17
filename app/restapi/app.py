from flask import Flask
from flask_graphql import GraphQLView
import graphene

from schema import schema

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

@app.route('/')
def index():
    return 'Welcome!'

if __name__ == '__main__':
    app.run()