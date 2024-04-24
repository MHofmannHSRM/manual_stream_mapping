from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import ProcessorSerializer, SenderSerializer, ReceiverSerializer, StreamSerializer


class ProcessorViewSet(NetBoxModelViewSet):
    queryset = models.Processor.objects.prefetch_related('tags')
    serializer_class = ProcessorSerializer
    filterset_class = filtersets.ProcessorFilterSet


class SenderViewSet(NetBoxModelViewSet):
    queryset = models.Sender.objects.prefetch_related('tags')
    serializer_class = SenderSerializer
    filterset_class = filtersets.SenderFilterSet


class ReceiverViewSet(NetBoxModelViewSet):
    queryset = models.Receiver.objects.prefetch_related('tags')
    serializer_class = ReceiverSerializer
    filterset_class = filtersets.ReceiverFilterSet


class StreamViewSet(NetBoxModelViewSet):
    queryset = models.Stream.objects.prefetch_related('tags')
    serializer_class = StreamSerializer
    filterset_class = filtersets.StreamFilterSet
