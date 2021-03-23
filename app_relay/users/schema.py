import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField

from .models import User
from .modules import UserObject
from utils.utils import MyConnectionField

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_users = MyConnectionField(UserObject,
    username=graphene.String())