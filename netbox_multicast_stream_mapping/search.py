from netbox.search import SearchIndex, register_search
from .models import Processor, Endpoint # todo


@register_search
class ProcessorIndex(SearchIndex):
    model = Processor
    fields = (
        ('name', 100),
        ('device', 100),
        ('module', 100),
        ('description', 500),
        ('comments', 5000),
    )


# todo sender
# todo receiver
# todo stream
