from netbox.views import generic
from utilities.views import ViewTab, register_model_view
from . import filtersets, forms, models, tables
from .models import Processor, Endpoint
from dcim.models import Device
from .tables import EndpointTable, ProcessorTable
from django.db.models import Count


# detail view
class ProcessorView(generic.ObjectView):
    queryset = models.Processor.objects.all()

    def get_extra_context(self, request, instance):
        endpoints = instance.endpoint_set.all()

        table = tables.EndpointTable(endpoints)
        table.configure(request)

        return {
            'endpoints_table': table,
        }


# list view
class ProcessorListView(generic.ObjectListView):
    queryset = models.Processor.objects.annotate(endpoint_count=Count('endpoint'))# TODO
    table = tables.ProcessorTable
    filterset = filtersets.ProcessorFilterSet
    filterset_form = forms.ProcessorFilterForm


# edit view
class ProcessorEditView(generic.ObjectEditView):
    queryset = models.Processor.objects.all()
    form = forms.ProcessorForm


class ProcessorBulkEditView(generic.BulkEditView):
    # queryset = Processor.objects.add_related_count(Processor.objects.all(), Processor, 'group', 'wirelesslan_count', cumulative=True)
    queryset = models.Processor.objects.all()
    filterset = filtersets.ProcessorFilterSet
    table = tables.ProcessorTable
    form = forms.ProcessorBulkEditForm # todo


# delete view
class ProcessorDeleteView(generic.ObjectDeleteView):
    queryset = models.Processor.objects.all()


class ProcessorBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Processor.objects.prefetch_related("tags")
    filterset = filtersets.ProcessorFilterSet
    table = tables.ProcessorTable


# ----------------------------------------------------------------------------------------------------------------------


# detail view
class EndpointView(generic.ObjectView):
    queryset = models.Endpoint.objects.all()


# list view
class EndpointListView(generic.ObjectListView):
    queryset = models.Endpoint.objects.all()
    table = tables.EndpointTable
    filterset = filtersets.EndpointFilterSet
    filterset_form = forms.EndpointFilterForm


# edit view
class EndpointEditView(generic.ObjectEditView):
    queryset = models.Endpoint.objects.all()
    form = forms.EndpointForm


class EndpointBulkEditView(generic.BulkEditView):
    # queryset = Processor.objects.add_related_count(Processor.objects.all(), Processor, 'group', 'wirelesslan_count', cumulative=True)
    queryset = models.Endpoint.objects.all()
    filterset = filtersets.EndpointFilterSet
    table = tables.EndpointTable
    form = forms.EndpointBulkEditForm  # todo


# delete view
class EndpointDeleteView(generic.ObjectDeleteView):
    queryset = models.Endpoint.objects.all()


class EndpointBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Endpoint.objects.prefetch_related("tags")
    filterset = filtersets.EndpointFilterSet
    table = tables.EndpointTable

# ----------------------------------------------------------------------------------------------------------------------


# detail view
class StreamView(generic.ObjectView):
    queryset = models.Stream.objects.all()


# list view
class StreamListView(generic.ObjectListView):
    queryset = models.Stream.objects.all()
    # für logik
    # queryset = models.AccessList.objects.annotate(rule_count=Count('rules'))
    table = tables.StreamTable
    filterset = filtersets.StreamFilterSet
    filterset_form = forms.StreamFilterForm


# edit view
class StreamEditView(generic.ObjectEditView):
    queryset = models.Stream.objects.all()
    form = forms.StreamForm


class StreamBulkEditView(generic.BulkEditView):
    # queryset = Processor.objects.add_related_count(Processor.objects.all(), Processor, 'group', 'wirelesslan_count', cumulative=True)
    queryset = models.Stream.objects.all()
    filterset = filtersets.StreamFilterSet
    table = tables.StreamTable
    form = forms.StreamBulkEditForm  # todo


# delete view
class StreamDeleteView(generic.ObjectDeleteView):
    queryset = models.Stream.objects.all()


class StreamBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Stream.objects.prefetch_related("tags")
    filterset = filtersets.StreamFilterSet
    table = tables.StreamTable

# ----------------------------------------------------------------------------------------------------------------------


# detail view
class FormatView(generic.ObjectView):
    queryset = models.Format.objects.all()


# list view
class FormatListView(generic.ObjectListView):
    queryset = models.Format.objects.all()
    table = tables.FormatTable
    # filterset = filtersets.StreamFilterSet
    # filterset_form = forms.StreamFilterForm


# edit view
class FormatEditView(generic.ObjectEditView):
    queryset = models.Format.objects.all()
    form = forms.FormatForm


class FormatBulkEditView(generic.BulkEditView):
    # queryset = Processor.objects.add_related_count(Processor.objects.all(), Processor, 'group', 'wirelesslan_count', cumulative=True)
    queryset = models.Format.objects.all()
    filterset = filtersets.FormatFilterSet
    table = tables.FormatTable
    form = forms.FormatBulkEditForm  # todo


# delete view
class FormatDeleteView(generic.ObjectDeleteView):
    queryset = models.Format.objects.all()


class FormatBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Format.objects.prefetch_related("tags")
    filterset = filtersets.FormatFilterSet
    table = tables.FormatTable


# ----------------------------------------------------------------------------------------------------------------------

# todo spalte in device list view?
# processor view for devices
@register_model_view(model=Device, name='Processors', path='processors')
class DeviceProcessorView(generic.ObjectChildrenView):
    queryset = Device.objects.all()
    child_model = Processor
    table = tables.ProcessorTable
    filterset = filtersets.ProcessorFilterSet
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
    queryset = models.Processor.objects.all().prefetch_related('endpoint_set')
    child_model = models.Endpoint
    table = tables.EndpointTable
    template_name = "netbox_multicast_stream_mapping/endpoint_list.html"

    def get_children(self, request, parent):
        return parent.endpoint_set.all()
