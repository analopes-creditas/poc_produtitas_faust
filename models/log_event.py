from faust import Record


class LogEvent(Record, serializer='json'):
    """ Describes a type of model that is an event log """

    severity: str
    message: str
    timestamp: float
    optional_field: str = 'default value'
