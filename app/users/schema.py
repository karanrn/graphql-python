import graphene

from .models import User
from .modules import UserObject

class Query(graphene.ObjectType):
    # node = graphene.relay.Node.Field()
    all_users = graphene.List(UserObject, search=graphene.String())

    def resolve_all_users(self, info, search=None, **kwargs):
        if search:
            # Search both username and email
            filter_user = (
                User.username.like('%'+search+"%") | 
                User.email.like('%'+search+"%")
            )
            return User.query.filter(filter_user).all()
        return User.query.all()
    # all_books = SQLAlchemyConnectionField(BookObject.connection)
    # all_users = SQLAlchemyConnectionField(UserObject.connection)