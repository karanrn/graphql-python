import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy import SQLAlchemyConnectionField

from Models import Book
from Models import User

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