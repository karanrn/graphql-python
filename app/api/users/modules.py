import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from .models import User
from database import db_session

class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        #interfaces = (graphene.relay.Node, )

class AddUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        email = graphene.String(required=True)
    
    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username, email):
        ifUser = User.query.filter_by(username=username).first()
        if ifUser is not None:
            raise Exception('user exists!')
        user = User(username=username, email=email)
        db_session.add(user)
        db_session.commit()
        return AddUser(user=user)