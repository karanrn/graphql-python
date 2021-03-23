import graphene

from .models import Book
from .modules import BookObject
from utils.utils import MyConnectionField

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_books = MyConnectionField(BookObject,
    title = graphene.String(),
    year = graphene.Int())