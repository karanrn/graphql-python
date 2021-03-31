from graphene_sqlalchemy import SQLAlchemyConnectionField

class MyConnectionField(SQLAlchemyConnectionField):
    # Below attributes/fields are for pagination and implemented by relay 
    RELAY_ARGS = ['first', 'last', 'before', 'after']

    @classmethod
    def get_query(cls, model, info, **args):
        query = super(MyConnectionField, cls).get_query(model, info, **args)
        for field, value in args.items():
            if field not in cls.RELAY_ARGS:
                query = query.filter(getattr(model, field) == value)
        return query