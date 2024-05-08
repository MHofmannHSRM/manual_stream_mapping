from django.db.models import Count
from utilities.views import ViewTab, register_model_view
from netbox.views import generic

from .models import *
from .tables import *
from .filtersets import *
from .forms import *
from dcim.models import Device
# todo suche geht nicht (?)
# todo in allen lösch/edit ansichten filter und filterset

# Format ---------------------------------------------------------------------------------------------------------------


# detail view
class FormatView(generic.ObjectView):
    queryset = Format.objects.all()


# list view
class FormatListView(generic.ObjectListView):
    queryset = Format.objects.all()
    table = FormatTable
    filterset = FormatFilterSet
    filterset_form = FormatFilterForm


# edit view
class FormatEditView(generic.ObjectEditView):
    queryset = Format.objects.all()
    form = FormatForm


class FormatBulkEditView(generic.BulkEditView):
    queryset = Format.objects.all()
    filterset = FormatFilterSet

    table = FormatTable
    form = FormatBulkEditForm


# delete view
class FormatDeleteView(generic.ObjectDeleteView):
    queryset = Format.objects.all()


class FormatBulkDeleteView(generic.BulkDeleteView):
    queryset = Format.objects.prefetch_related("tags")
    filterset = FormatFilterSet
    table = FormatTable


# Processor ------------------------------------------------------------------------------------------------------------


# detail view
class ProcessorView(generic.ObjectView):
    queryset = Processor.objects.all()

    def get_extra_context(self, request, instance):
        endpoints = instance.endpoint_set.all()

        table = EndpointTable(endpoints)
        table.configure(request)

        return {'endpoints_table': table, }


# list view
class ProcessorListView(generic.ObjectListView):
    queryset = Processor.objects.annotate(endpoint_count=Count('endpoint'))# TODO
    table = ProcessorTable
    filterset = ProcessorFilterSet
    filterset_form = ProcessorFilterForm


# edit view
class ProcessorEditView(generic.ObjectEditView):
    queryset = Processor.objects.all()
    form = ProcessorForm


class ProcessorBulkEditView(generic.BulkEditView):
    queryset = Processor.objects.all()
    filterset = ProcessorFilterSet
    table = ProcessorTable
    form = ProcessorBulkEditForm


# delete view
class ProcessorDeleteView(generic.ObjectDeleteView):
    queryset = Processor.objects.all() # todo count funktion?
# todo alle farben in ansichten?


class ProcessorBulkDeleteView(generic.BulkDeleteView):
    queryset = Processor.objects.prefetch_related("tags")
    filterset = ProcessorFilterSet
    table = ProcessorTable


# Endpoint -------------------------------------------------------------------------------------------------------------


# detail view
class EndpointView(generic.ObjectView):
    queryset = Endpoint.objects.all()


# list view
class EndpointListView(generic.ObjectListView):
    queryset = Endpoint.objects.all()
    table = EndpointTable
    filterset = EndpointFilterSet
    filterset_form = EndpointFilterForm


# edit view
class EndpointEditView(generic.ObjectEditView):
    queryset = Endpoint.objects.all()
    form = EndpointForm


class EndpointBulkEditView(generic.BulkEditView):
    queryset = Endpoint.objects.all()
    filterset = EndpointFilterSet
    table = EndpointTable
    form = EndpointBulkEditForm


# delete view
class EndpointDeleteView(generic.ObjectDeleteView):
    queryset = Endpoint.objects.all()


class EndpointBulkDeleteView(generic.BulkDeleteView):
    queryset = Endpoint.objects.prefetch_related("tags")
    filterset = EndpointFilterSet
    table = EndpointTable


# Stream ---------------------------------------------------------------------------------------------------------------


# detail view
class StreamView(generic.ObjectView):
    queryset = Stream.objects.all()


# list view
class StreamListView(generic.ObjectListView):
    queryset = Stream.objects.all()
    # für logik
    # queryset = models.AccessList.objects.annotate(rule_count=Count('rules'))
    table = StreamTable
    filterset = StreamFilterSet
    filterset_form = StreamFilterForm


# edit view
class StreamEditView(generic.ObjectEditView):
    queryset = Stream.objects.all()
    form = StreamForm


class StreamBulkEditView(generic.BulkEditView):
    queryset = Stream.objects.all()
    filterset = StreamFilterSet
    table = StreamTable
    form = StreamBulkEditForm


# delete view
class StreamDeleteView(generic.ObjectDeleteView):
    queryset = Stream.objects.all()


class StreamBulkDeleteView(generic.BulkDeleteView):
    queryset = Stream.objects.prefetch_related("tags")
    filterset = StreamFilterSet
    table = StreamTable


# Other ----------------------------------------------------------------------------------------------------------------


# todo spalte in device list view?
# processor view for devices
@register_model_view(model=Device, name='Processors', path='processors')
class DeviceProcessorView(generic.ObjectChildrenView):
    queryset = Device.objects.all()
    child_model = Processor
    table = ProcessorTable
    filterset = ProcessorFilterSet
    template_name = 'netbox_multicast_stream_mapping/processor_list.html'

    tab = ViewTab(
        label="Processors",
        weight=100,
        badge=lambda obj: Processor.objects.filter(device=obj).count(),
    )

    def get_children(self, request, instance):
        return Processor.objects.filter(device=instance).annotate(endpoint_count=Count('endpoint'))


# endpoint view for single processor
class EndpointChildView(generic.ObjectChildrenView):
    queryset = Processor.objects.all().prefetch_related('endpoint_set')
    child_model = Endpoint
    table = EndpointTable
    template_name = "netbox_multicast_stream_mapping/endpoint_list.html"

    def get_children(self, request, parent):
        return parent.endpoint_set.all()
