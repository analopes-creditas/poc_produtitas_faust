from faust import Record
import core.utils.constants as const


class DataProductEvent(Record, serializer=const.SERIALIZER, validation=True):
    """ Describes a model type that is a data product at creation """

    ...
