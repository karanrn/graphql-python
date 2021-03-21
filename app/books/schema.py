import graphene

from .models import Book
from .modules import BookObject

class Query(graphene.ObjectType):
    # node = graphene.relay.Node.Field()
    all_books = graphene.List(BookObject, 
    search=graphene.String(),
    first=graphene.Int(),
    skip=graphene.Int())

    def resolve_all_books(self, info, first=None, skip=None, search=None, **kwargs):
        result = []
        if search:
            # Search both title and description
            filter_book = (
                Book.title.like('%'+search+'%') |
                Book.description.like('%'+search+'%') 
            )
            result = Book.query.filter(filter_book).all()
        else:
            result = Book.query.all()
      
        if skip:
            # skips first n items
            result = result[skip:]
        
        if first:
            # returns first n items from result
            result = result[:first]
    
        return result
    # all_books = SQLAlchemyConnectionField(BookObject.connection)
    # all_users = SQLAlchemyConnectionField(UserObject.connection)