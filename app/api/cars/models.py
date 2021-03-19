import graphene
from collections import namedtuple

class CarType(graphene.ObjectType):
    id = graphene.Int()
    plateNumber = graphene.String()
    color = graphene.String()
    model = graphene.String()
    chasisNumber = graphene.String()
    status = graphene.String()
    productionYear = graphene.Int()
    issueDate = graphene.Date()
    expiryDate = graphene.Date()

    def __init__(self, id, plateNumber, color, model, chasisNumber, status, 
    productionYear, issueDate, expiryDate):
        self.id = id
        self.plateNumber = plateNumber
        self.color = color
        self.model = model
        self.chasisNumber = chasisNumber
        self.status = status
        self.productionYear = productionYear
        self.issueDate = issueDate
        self.expiryDate = expiryDate

def CarTypeDecoder(carDict):
    return namedtuple('X', carDict.keys())(*carDict.values())

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_cars = graphene.List(CarType, plateNumber=graphene.String())

    def resolve_all_cars(self, info, plateNumber=None, **kwargs):
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

schema = graphene.Schema(query=Query)