from netbox.filtersets import NetBoxModelFilterSet
from .models import Processor, Sender, Receiver, Stream


class ProcessorFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Processor
        fields = ('id', 'name', 'device', 'module')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class SenderFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Sender
        fields = ('id', 'name') # TODO

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class ReceiverFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Receiver
        fields = ('id', 'name') # TODO

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class StreamFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Stream
        fields = ('id', 'name') # TODO

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
