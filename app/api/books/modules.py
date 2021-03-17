import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import Book
from database import db_session
from users.models import User

class BookObject(SQLAlchemyObjectType):
    class Meta:
        model = Book
        #interfaces = (graphene.relay.Node, )

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

class DeleteBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
    
    book = graphene.Field(lambda: BookObject)

    def mutate(self, info, title):
        book = Book.query.filter_by(title=title).first()
        if book is None:
            raise Exception('book does not exist in the catalogue!')
        db_session.delete(book)
        db_session.commit()
        return DeleteBook(book=book)