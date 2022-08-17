from faust import Record


class DataProductCreate(Record, serializer='json', validation=True):
    """ Describes a model type that is a data product at creation """

    type_dp: str
    owner: str
    name: str
    description: str = None


class DataProductUpdate(Record, serializer='json', validation=True):
    """ Describes a model type that is a data product on update """
    
    ...
