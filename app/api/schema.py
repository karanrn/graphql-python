import graphene

from books.models import Book
from books.modules import BookObject, AddBook
from users.models import User
from users.modules import UserObject, AddUser

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = graphene.List(UserObject, search=graphene.String())
    all_books = graphene.List(BookObject, search=graphene.String())

    def resolve_all_users(self, info, search=None, **kwargs):
        if search:
            # Search both username and email
            filter_user = (
                User.username.like('%'+search+"%") | 
                User.email.like('%'+search+"%")
            )
            return User.query.filter(filter_user).all()
        return User.query.all()

    def resolve_all_books(self, info, search=None, **kwargs):
        if search:
            # Search both title and description
            filter_book = (
                Book.title.like('%'+search+'%') |
                Book.description.like('%'+search+'%') 
            )
            return Book.query.filter(filter_book).all()
        return Book.query.all()
    # all_books = SQLAlchemyConnectionField(BookObject.connection)
    # all_users = SQLAlchemyConnectionField(UserObject.connection)

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_book = AddBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)