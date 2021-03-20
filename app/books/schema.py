import graphene

from .models import Book
from .modules import BookObject

class Query(graphene.ObjectType):
    # node = graphene.relay.Node.Field()
    all_books = graphene.List(BookObject, search=graphene.String())

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