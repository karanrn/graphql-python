import graphene
import json
import requests

import app.books.schema
from app.books.modules import AddBook, DeleteBook
import app.users.schema
from app.users.modules import AddUser
import app.cars.schema

class Query(app.users.schema.Query, app.books.schema.Query, app.cars.schema.Query):
    pass

class Mutation(graphene.ObjectType):
    add_user = AddUser.Field()
    add_book = AddBook.Field()
    delete_book = DeleteBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)