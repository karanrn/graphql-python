import graphene

from books.models import Book
from books.modules import BookObject, AddBook
from users.models import User
from users.modules import UserObject, AddUser

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = graphene.List(UserObject)
    all_books = graphene.List(BookObject)

    def resolve_all_users(self, info, **kwargs):
        return User.query.all()

    def resolve_all_books(self, info, **kwargs):
        return Book.query.all()
    # all_books = SQLAlchemyConnectionField(BookObject.connection)
    # all_users = SQLAlchemyConnectionField(UserObject.connection)

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_book = AddBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)