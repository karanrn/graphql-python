import graphene
import json
import requests

from .models import CarType, CarTypeDecoder

class Query(graphene.ObjectType):
    # node = graphene.relay.Node.Field()
    all_cars = graphene.List(CarType, plateNumber=graphene.String())
    
    def resolve_all_cars(self, info, plateNumber=None, **kwargs):
        ''' Querying from REST API '''
        base_url = 'https://mvrp.herokuapp.com/api/'
        if plateNumber is None:
            url = base_url + 'cars/'
            response = requests.get(url)
            carList = json.loads(response.text, object_hook=CarTypeDecoder)
        else:
            url = base_url + 'car?plateNumber=' + str(plateNumber)
            response = requests.get(url)
            carList = []
            carList.append(json.loads(response.text, object_hook=CarTypeDecoder))
        return carList
    # all_books = SQLAlchemyConnectionField(BookObject.connection)
    # all_users = SQLAlchemyConnectionField(UserObject.connection)