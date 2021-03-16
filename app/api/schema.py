import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql import GraphQLError

from books.models import Book
from users.models import User
from database import db_session

class BookObject(SQLAlchemyObjectType):
    class Meta:
        model = Book
        #interfaces = (graphene.relay.Node, )

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        #interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    #node = graphene.relay.Node.Field()
    all_users = graphene.List(UserObject)
    all_books = graphene.List(BookObject)

    def resolve_all_users(self, info, **kwargs):
        return User.query.all()

    def resolve_all_books(self, info, **kwargs):
        return Book.query.all()
    # all_books = SQLAlchemyConnectionField(BookObject.connection)
    # all_users = SQLAlchemyConnectionField(UserObject.connection)

class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
    
    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username, email):
        ifUser = User.query.filter_by(username=username).first()
        if ifUser is not None:
            raise Exception('User exists!')
        user = User(username=username, email=email)
        db_session.add(user)
        db_session.commit()
        return AddUser(user=user)

class AddBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        year = graphene.Int(required=True)
        username = graphene.String(required=True)
    
    book = graphene.Field(lambda: BookObject)

    def mutate(self, info, title, description, year, username):
        user = User.query.filter_by(username=username).first()
        book = Book(title=title, description=description, year=year)
        if user is not None:
            book.author_id = user.id
        db_session.add(book)
        db_session.commit()
        return AddBook(book=book)

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_book = AddBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)