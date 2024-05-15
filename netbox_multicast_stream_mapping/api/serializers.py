from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ipam.api.serializers import NestedPrefixSerializer

from ..models import Processor, Endpoint, Stream, Format


class NestedProcessorSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:processor-detail')

    class Meta:
        model = Processor
        fields = ('id', 'url', 'display', 'name')


class ProcessorSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:processor-detail')

    # todo access_list = NestedAccessListSerializer()
    # todo andere modlle     source_prefix = NestedPrefixSerializer()
    # todo rules count

    class Meta:
        model = Processor
        fields = (
            'id', 'url', 'display', 'name', 'device', 'module', 'description',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )


# class NestedMulticastSenderSerializer(WritableNestedSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:multicast_sender-detail')
#
#     class Meta:
#         model = MulticastSender
#         fields = ('id', 'url', 'display', 'name')
#


# TODO Nested Endpojnt + alle?


class EndpointSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:endpoint-detail')

    # todo access_list = NestedAccessListSerializer()
    # todo andere modlle     source_prefix = NestedPrefixSerializer()
    # todo rules count

    class Meta:
        model = Endpoint
        fields = (
            'id', 'url', 'display', 'name', 'device', 'processor', 'endpoint_type', 'primary_ip', 'secondary_ip',
            'max_bandwidth', 'supported_formats', 'switch_method', 'signal_type', 'comments', 'description', 'tags',
            'custom_fields', 'created', 'last_updated',
        )


class StreamSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:stream-detail')

    # todo access_list = NestedAccessListSerializer()
    # todo andere modlle     source_prefix = NestedPrefixSerializer()
    # todo rules count

    class Meta:
        model = Stream
        fields = (
            'id', 'url', 'display', 'name', 'sender', 'receivers', 'bandwidth', 'formats', 'signal_type',
            'comments', 'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )


# todo
class FormatSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:format-detail')

    class Meta:
        model = Format
        fields = (
            'id', 'url', 'display', 'name', 'type', 'res_h', 'res_w', 'fps', 'audio_ch', 'comments', 'description',
            'custom_fields', 'created', 'last_updated',
        )
