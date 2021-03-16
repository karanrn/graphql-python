import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy import SQLAlchemyConnectionField

from books.models import Book
from users.models import User
from database import db_session

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
    all_books = SQLAlchemyConnectionField(BookObject.connection)
    all_users = SQLAlchemyConnectionField(UserObject.connection)

class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
    
    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username, email):
        user = User(username=username, email=email)
        db_session.add(user)
        db_session.commit()
        return AddUser(user=user)

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)