# import django_filters
from netbox.filtersets import NetBoxModelFilterSet
from .models import *
# todo TagFilter?
# todo auch in bulk edit/bulkd delete
# todo auch rest api filterset_class


class FormatFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Format
        fields = ('id', 'name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'port', 'description')  # TODO

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class ProcessorFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Processor
        fields = ('id', 'name', 'device', 'module', 'description')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class EndpointFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Endpoint
        fields = (
            'id', 'name', 'device', 'processor', 'interface', 'endpoint_type', 'primary_ip', 'secondary_ip',
            'max_bandwidth', 'supported_formats', 'switch_method', 'signal_type', 'description'
        )

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)


class StreamFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Stream
        fields = ('id', 'name', 'sender', 'receivers', 'bandwidth', 'signal_type', 'protocol', 'formats', 'description')

    def search(self, queryset, name, value):
        return queryset.filter(description__icontains=value)
