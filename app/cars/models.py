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