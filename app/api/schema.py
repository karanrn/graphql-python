import graphene

import users.schema
import books.schema

class Query(
    users.schema.Query,
    books.schema.Query,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query)
