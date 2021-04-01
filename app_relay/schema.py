import graphene
import json
import requests

import app_relay.books.schema
from app_relay.books.modules import AddBook, DeleteBook
import app_relay.users.schema
from app_relay.users.modules import AddUser
import app_relay.cars.schema

class Query(app_relay.users.schema.Query, app_relay.books.schema.Query, app_relay.cars.schema.Query):
    pass

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_book = AddBook.Field()
    delete_book = DeleteBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)