from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Processor, Sender, Receiver, Stream, Format
from ipam.api.serializers import NestedPrefixSerializer


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
            'id', 'url', 'display', 'name', 'device', 'module', 'sender_count', 'receiver_count', 'description',
            'comments', 'tags', 'custom_fields', 'created', 'last_updated',
        )


# class NestedMulticastSenderSerializer(WritableNestedSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:multicast_sender-detail')
#
#     class Meta:
#         model = MulticastSender
#         fields = ('id', 'url', 'display', 'name')
#

class SenderSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:sender-detail')

    # todo access_list = NestedAccessListSerializer()
    # todo andere modlle     source_prefix = NestedPrefixSerializer()
    # todo rules count

    class Meta:
        model = Sender
        fields = (
            'id', 'url', 'display', 'name', 'processor', 'sender_ip', 'max_bandwidth_out',
            'supported_formats', 'signal_type', 'comments', 'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )


class ReceiverSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:receiver-detail')

    # todo access_list = NestedAccessListSerializer()
    # todo andere modlle     source_prefix = NestedPrefixSerializer()
    # todo rules count

    class Meta:
        model = Receiver
        fields = (
            'id', 'url', 'display', 'name', 'processor', 'receiver_ip', 'max_bandwidth_in',
            'supported_formats', 'signal_type', 'comments', 'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )


class StreamSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:stream-detail')

    # todo access_list = NestedAccessListSerializer()
    # todo andere modlle     source_prefix = NestedPrefixSerializer()
    # todo rules count

    class Meta:
        model = Stream
        fields = (
            'id', 'url', 'display', 'name', 'processor', 'sender', 'receivers', 'bandwidth', 'format', 'signal_type',
            'protocol', 'audio_channels', 'comments', 'description', 'tags', 'custom_fields', 'created', 'last_updated',
        )


class FormatSerializer(NetBoxModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='plugins-api:netbox_multicast_stream_mapping-api:format-detail')

    class Meta:
        model = Format
        fields = (
            'id', 'url', 'display', 'name', 'comments', 'description', 'custom_fields', 'created', 'last_updated',
        )
