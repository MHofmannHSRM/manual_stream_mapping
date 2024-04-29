from netbox.filtersets import NetBoxModelFilterSet
from .models import Processor, Endpoint, Stream


class ProcessorFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Processor
        fields = ('id', 'name', 'device', 'module')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class EndpointFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Endpoint
        fields = ('id', 'name') # TODO

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class StreamFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Stream
        fields = ('id', 'name') # TODO

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
