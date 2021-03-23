import graphene
import json
import requests

import books.schema
from books.modules import AddBook, DeleteBook
import users.schema
from users.modules import AddUser
import cars.schema

class Query(users.schema.Query, books.schema.Query, cars.schema.Query):
    pass

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_book = AddBook.Field()
    delete_book = DeleteBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)