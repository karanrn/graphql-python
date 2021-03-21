import graphene

from .models import User
from .modules import UserObject

class Query(graphene.ObjectType):
    # node = graphene.relay.Node.Field()
    all_users = graphene.List(UserObject, 
    search=graphene.String(),
    first=graphene.Int(),
    skip=graphene.Int())

    def resolve_all_users(self, info, first=None, skip=None, search=None, **kwargs):
        result = []
        if search:
            # Search both username and email
            filter_user = (
                User.username.like('%'+search+"%") | 
                User.email.like('%'+search+"%")
            )
            result = User.query.filter(filter_user).all()
        else:
            result = User.query.all()
        if skip:
            # skips first n items
            result = result[skip:]
        
        if first:
            # returns first n items from result
            result = result[:first]
    
        return result
    # all_books = SQLAlchemyConnectionField(BookObject.connection)
    # all_users = SQLAlchemyConnectionField(UserObject.connection)